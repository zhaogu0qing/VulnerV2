# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pymongo
from pybloom_live import BloomFilter
from scrapy.exceptions import DropItem

class MongoPipeline(object):

    collection_name = 'Vulner'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'zgq')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # print(self.mongo_uri, self.mongo_db)
        print('[SAVE to %s]' % self.collection_name, item['url'])
        self.db[self.collection_name].insert(dict(item))
        count = item['count']
        del item['count']
        if count > 10:
            spider.crawler.engine.close_spider(spider, 'have crawl 1000')
        return item


class BloomFilterPipeline(object):
    def __init__(self):
        self.file_name = 'cnnvd_bloomfilter.blm'

    def open_spider(self, spider):
        if os.path.exists(self.file_name):
            self.bf = BloomFilter.fromfile(open(self.file_name, 'rb'))
            print('open blm file success')
        else:
            self.bf = BloomFilter(100000, 0.001)
            print('create a new blm file')

    def process_item(self, item, spider):
        if item['url'] in self.bf:
            print('drop one item for exist', item['url'])
            raise DropItem('drop an item for exist')
        else:
            self.bf.add(item['url'])
            return item

    def close_spider(self, spider):
        self.bf.tofile(open(self.file_name, 'wb'))
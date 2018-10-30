# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from bs4 import BeautifulSoup

class CnnvdmainSpider(CrawlSpider):
    name = 'cnnvdMain'
    allowed_domains = ['cnnvd.org.cn']
    start_urls = ['http://cnnvd.org.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'/web/xxk/ldxqById.tag?.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['url'] = response.url
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        for link in BeautifulSoup(str(response.body), 'lxml').find_all('a'):
            href = re.search(r"(/web/vulnerability/querylist\.tag\?pageno=\d+&repairLd=)", str(link))
            if href:
                print(link)
                yield Request('http://cnnvd.org.cn/' + href.group(1))
        print(i)
        # return i

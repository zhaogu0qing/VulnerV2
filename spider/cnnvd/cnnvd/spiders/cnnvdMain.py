# -*- coding: utf-8 -*-
import re
import time

import sys
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from items import VulnerabilityItem

class CnnvdmainSpider(Spider):
    name = 'cnnvdMain'
    allowed_domains = ['cnnvd.org.cn']
    start_urls = [
        # 'http://cnnvd.org.cn/',
        'http://cnnvd.org.cn/web/vulnerability/querylist.tag'
                  ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = 'http://cnnvd.org.cn'
        self.count = 0

    @staticmethod
    def wash_field(text):
        text = re.sub(r'<[^>]*?>', '', text, re.S | re.M)
        text = text.replace('\r', '').replace('\n', '').replace('\t', '').strip()
        return text

    def parse(self, response):
        links = response.xpath('.//a')
        for link in links:
            href = str(link.attrib.get('href'))
            onclick = str(link.attrib.get('onclick'))
            onclickRe = re.compile(r'(/web/vulnerability/querylist\.tag\?pageno=\d+&repairLd=)')
            if re.search(r'/web/xxk/ldxqById\.tag\?.*', href):
                # print('[link]', href)
                yield Request(self.host + href, callback=self.parse_vulner)
            elif href == 'javascript:void(0)' and onclickRe.search(onclick):
                href = onclickRe.search(onclick).group(1)
                # print('[link]', href)
                yield Request(self.host + href, callback=self.parse)


    def parse_vulner(self, response):
        i = VulnerabilityItem()
        i['url'] = response.url
        i['title'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/h2/text()').extract()[0]
        i['CNNVDId'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[1]/span/text()').extract()[0].replace('CNNVD编号：', '')
        i['CVEId'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[3]/a/text()').extract()[0]
        i['publishTime'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[5]/a/text()').extract()[0]
        i['updateTime'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[7]/a/text()').extract()[0]
        i['vulnerSource'] = response.xpath('//*[@id="1"]/span/text()').extract()[0].replace('漏洞来源：', '')
        i['vulnerLevel'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[2]/span/text()').extract()[0].replace('危害等级：', '')
        i['vulnerType'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[4]/a/text()').extract()[0]
        i['threatType'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[6]/a/text()').extract()[0]
        i['firm'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[8]/span/text()').extract()[0].replace('厂\xa0\xa0\xa0\xa0\xa0\xa0\xa0商：', '')
        i['vulnerSummary'] = response.xpath('/html/body/div[4]/div/div[1]/div[3]').extract()[0].replace('漏洞简介', '')
        i['vulnerBulletin'] = response.xpath('/html/body/div[4]/div/div[1]/div[4]').extract()[0].replace('漏洞公告', '')
        i['vulnerReference'] = response.xpath('/html/body/div[4]/div/div[1]/div[5]').extract()[0].replace('参考网址', '')
        i['vulnerAffect'] = response.xpath('/html/body/div[4]/div/div[1]/div[6]').extract()[0].replace('受影响实体', '').replace('更多&gt;&gt;', '')
        i['vulnerPatch'] = response.xpath('/html/body/div[4]/div/div[1]/div[7]').extract()[0].replace('补丁', '')
        i['tag'] = ''
        i['source'] = 'cnnvd'
        for k, v in i.items():
            i[k] = self.wash_field(i[k])
        # self.count += 1
        # if self.count > self.settings.attributes['MAX_COUNT']:
        #     print(self.settings.attributes['MAX_COUNT'])
        yield i


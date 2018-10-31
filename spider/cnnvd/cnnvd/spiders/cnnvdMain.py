# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.http import Request, Response
from bs4 import BeautifulSoup

class CnnvdmainSpider(Spider):
    name = 'cnnvdMain'
    allowed_domains = ['cnnvd.org.cn']
    start_urls = [
        # 'http://cnnvd.org.cn/',
        'http://cnnvd.org.cn/web/vulnerability/querylist.tag'
                  ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = 'http://cnnvd.org.cn/'

    def parse(self, response):
        links = response.xpath('.//a')
        for link in links:
            href = str(link.attrib.get('href'))
            onclick = str(link.attrib.get('onclick'))
            onclickRe = re.compile(r'(/web/vulnerability/querylist\.tag\?pageno=\d+&repairLd=)')
            if re.search(r'/web/xxk/ldxqById\.tag\?.*', href):
                print('[link]', href)
                yield Request(self.host + href, callback=self.parse_vulner)
            elif href == 'javascript:void(0)' and onclickRe.search(onclick):
                href = onclickRe.search(onclick).group(1)
                print('[link]', href)
                yield Request(self.host + href, callback=self.parse)


    def parse_vulner(self, response):
        i = {}
        i['title'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/h2/text()').extract()[0]
        print('[vuler]', i)

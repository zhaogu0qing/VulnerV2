# -*- coding: utf-8 -*-
import re
import time

import sys
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from items import VulnerabilityItem


class CnnvdDebugSpider(Spider):
    name = 'cnnvd_debug'
    allowed_domains = ['cnnvd.org.cn']
    start_urls = [
        'http://cnnvd.org.cn/web/vulnerability/querylist.tag'
                  ]

    def parse(self, response):
        links = response.xpath('.//a')
        for link in links:
            print(link)


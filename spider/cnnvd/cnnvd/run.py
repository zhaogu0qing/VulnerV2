# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/31 11:30
@Author  : zhaoguoqing600689
@File    : run.py
@Software: PyCharm
"""
from scrapy.crawler import CrawlerProcess
from spiders.cnnvdMain import CnnvdmainSpider


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(CnnvdmainSpider)
    process.start()
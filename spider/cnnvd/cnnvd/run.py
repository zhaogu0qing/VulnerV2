# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/31 11:30
@Author  : zhaoguoqing600689
@File    : run.py
@Software: PyCharm
"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.cnnvdMain import CnnvdmainSpider
import sys
if len(sys.argv) > 1:
    CONCURRENT_REQUESTS = sys.argv[1]
else:
    CONCURRENT_REQUESTS = 4

if __name__ == '__main__':
    config = get_project_settings().copy_to_dict()
    config['LOG_LEVEL'] = 'WARNING'
    config['DOWNLOAD_DELAY'] = 0
    # config['MAX_COUNT'] = 5
    config['CONCURRENT_REQUESTS'] = CONCURRENT_REQUESTS
    process = CrawlerProcess(config)
    process.crawl(CnnvdmainSpider)
    process.start()
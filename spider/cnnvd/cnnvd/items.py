# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnvdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class VulnerabilityItem(scrapy.Item):
    source = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    CNNVDId = scrapy.Field()
    CVEId = scrapy.Field()
    publishTime = scrapy.Field()
    updateTime = scrapy.Field()
    vulnerSource = scrapy.Field()
    vulnerLevel = scrapy.Field()
    vulnerType = scrapy.Field()
    threatType = scrapy.Field()
    firm = scrapy.Field()
    vulnerSummary = scrapy.Field()
    vulnerBulletin = scrapy.Field()
    vulnerReference = scrapy.Field()
    vulnerAffect = scrapy.Field()
    vulnerPatch = scrapy.Field()
    tag = scrapy.Field()




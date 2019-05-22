# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    RecruitPostName = scrapy.Field()
    BGName = scrapy.Field()
    LocationName = scrapy.Field()
    CategoryName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    Responsibility = scrapy.Field()
    Requirement = scrapy.Field()

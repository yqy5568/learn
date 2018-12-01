# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Uav81Item(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    post_time = scrapy.Field()
    from_lai = scrapy.Field()
    author = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    img_url = scrapy.Field()
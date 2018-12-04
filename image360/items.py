# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImageItem(Item):
    collection = table = 'image'  # 表的名称
    id = Field()
    url = Field()
    title = Field()

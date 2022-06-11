# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Book24Item(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    price_old = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    _id = scrapy.Field()

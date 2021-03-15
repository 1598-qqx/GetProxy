# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetproxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    scheme = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    category = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# encoding = utf8
import scrapy


class IqiyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    desc = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    actor = scrapy.Field()
    rating = scrapy.Field()
    rater = scrapy.Field()


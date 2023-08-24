# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from itemloaders.processors import Join, TakeFirst


class CCEItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image = scrapy.Field(output_processor=Join())
    title = scrapy.Field(output_processor=Join())
    author = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    text = scrapy.Field(output_processor=Join())

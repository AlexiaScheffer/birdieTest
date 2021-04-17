# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


# class StoresItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class StoresItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product = Field()
    price = Field()
    product_status = Field()
    store = Field()
    request_status = Field()
    url = Field()

# Define here the models for your scraped items

import scrapy


class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # only one field that it of Quote.
    Quote = scrapy.Field()

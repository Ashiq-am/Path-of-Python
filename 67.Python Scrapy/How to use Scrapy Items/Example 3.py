# Define here the models for your scraped
# items
# Import the required library
import scrapy


# Define the fields for Scrapy item here
# in class
class GfgSpiderreadingitemsItem(scrapy.Item):
    # Item key for Title of Quote
    quotetitle = scrapy.Field()

    # Item key for Author of Quote
    author = scrapy.Field()

    # Item key for Tags of Quote
    tags = scrapy.Field()

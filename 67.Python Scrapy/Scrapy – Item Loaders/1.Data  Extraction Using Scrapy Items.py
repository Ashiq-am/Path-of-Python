# Define here the models for your scraped item
import scrapy


# Item class name for the book title and price
class GfgItemloadersItem(scrapy.Item):
    # Scrape Book price
    price = scrapy.Field()

    # Scrape Book Title
    title = scrapy.Field()

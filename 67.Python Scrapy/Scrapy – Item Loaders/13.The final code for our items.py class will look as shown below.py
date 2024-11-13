# Define here the models for your scraped items

# import Scrapy library
import scrapy

# import itemloader methods
from itemloaders.processors import TakeFirst, MapCompose

# import remove_tags method to remove all tags present
# in the response
from w3lib.html import remove_tags


# custom method to replace '&' with 'AND'
# in book title
def replace_and_sign(value):
    # python replace method to replace '&' operator
    # with 'AND'
    return value.replace('&', ' AND ')


# custom method to remove the pound currency sign from
# book price
def remove_pound_sign(value):
    # for pound press Alt + 0163
    # python replace method to replace '£' with a blank
    return value.replace('£', '').strip()


# Item class to define all the Item fields - book title
# and price
class GfgItemloadersItem(scrapy.Item):
    # Assign the input and output processor for book price field
    price = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_pound_sign), output_processor=TakeFirst())

    # Assign the input and output processor for book title field
    title = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_and_sign), output_processor=TakeFirst())

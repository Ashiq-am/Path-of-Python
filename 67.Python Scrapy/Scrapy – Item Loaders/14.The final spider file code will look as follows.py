# Import the required Scrapy library
import scrapy

# Import the Item Loader library
from scrapy.loader import ItemLoader

# Import the items class from 'items.py' file
from ..items import GfgItemloadersItem


# Spider class having Item loader
class GfgLoadbookdataSpider(scrapy.Spider):
    # Name of the spider
    name = 'gfg_loadbookdata'

    # The domain to be scraped
    allowed_domains = [
        'books.toscrape.com/catalogue/category/books/womens-fiction_9']

    # The webpage to be scraped
    start_urls = [
        'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/']

    # Default callback method used by the spider
    # Data in the response will be processed here
    def parse(self, response):
        # Loop through all the books using XPath expression
        for books in response.xpath('//*[@class="product_pod"]'):
            # Define Item Loader object,
            # by passing item and selector attribute
            loader = ItemLoader(item=GfgItemloadersItem(), selector=books)

            # Item loader method add_xpath(),for price,
            # mention the field name and xpath expression
            loader.add_xpath('price', './/*[@class="product_price"]/p/text()')

            # Item loader method add_xpath(),
            # for title, mention the field name
            # and xpath expression
            loader.add_xpath('title', './/h3/a/@title')

            # use the load_item method of
            # loader to populate the parsed items
            yield loader.load_item()

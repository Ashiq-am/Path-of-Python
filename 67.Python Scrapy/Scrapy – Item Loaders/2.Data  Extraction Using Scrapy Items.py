# Import Scrapy library
import scrapy

# Import Item class
from ..items import GfgItemloadersItem


# Spider class name
class GfgLoadbookdataSpider(scrapy.Spider):
    # Name of the spider
    name = 'gfg_loadbookdata'

    # The domain to be scraped
    allowed_domains = [
        'books.toscrape.com/catalogue/category/books/womens-fiction_9']

    # The URL to be scraped
    start_urls = [
        'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/']

    # Default parse callback method
    def parse(self, response):
        # Create an object of Item class
        item = GfgItemloadersItem()

        # loop through all books
        for books in response.xpath('//*[@class="product_pod"]'):
            # XPath expression for the book price
            price = books.xpath(
                './/*[@class="product_price"]/p/text()').extract_first()

            # place price value in item key
            item['price'] = price

            # XPath expression for the book title
            title = books.xpath('.//h3/a/text()').extract()

            # place title value in item key
            item['title'] = title

            # yield the item
            yield item

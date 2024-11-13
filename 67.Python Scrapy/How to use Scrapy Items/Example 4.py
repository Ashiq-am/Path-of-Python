# Import the required library
import scrapy

# Import the Item class with fields
# mentioned in the items.py file
from ..items import GfgSpiderreadingitemsItem


class GfgSpiitemsreadSpider(scrapy.Spider):
    name = 'gfg_spiitemsread'
    allowed_domains = ['quotes.toscrape.com/tag/reading']
    start_urls = ['http://quotes.toscrape.com/tag/reading/']

    def parse(self, response):
        # Write XPath expression to loop through
        # all quotes
        quotes = response.xpath('//*[@class="quote"]')

        # Loop through all quotes
        for quote in quotes:
            # Create an object of Item class
            item = GfgSpiderreadingitemsItem()

            # XPath expression to fetch text of the
            # Quote title Store the title in the class
            # attribute in key-value pair
            item['quotetitle'] = quote.xpath(
                './/*[@class="text"]/text()').extract_first()

            # XPath expression to fetch author of the Quote
            # Store the author in the class attribute in
            # key-value pair
            item['author'] = quote.xpath(
                './/*[@itemprop="author"]/text()').extract()

            # XPath expression to fetch tags of the Quote title
            # Store the tags in the class attribute in key-value
            # pair
            item['tags'] = quote.xpath(
                './/*[@itemprop="keywords"]/@content').extract()

            # Yield the item object
            yield item

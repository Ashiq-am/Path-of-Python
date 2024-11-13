# Import the required library
import scrapy


# The Spider class
class GfgSpiitemsreadSpider(scrapy.Spider):
    # Name of the spider
    name = 'gfg_spiitemsread'

    # The domain allowed to scrape
    allowed_domains = ['quotes.toscrape.com/tag/reading']

    # The URL to be scraped
    start_urls = ['http://quotes.toscrape.com/tag/reading/']

    # Default callback function
    def parse(self, response):
        # Fetch all quotes tags
        quotes = response.xpath('//*[@class="quote"]')

        # Loop through the Quote selector elements
        # to get details of each
        for quote in quotes:
            # XPath expression to fetch text of the Quote title
            title = quote.xpath('.//*[@class="text"]/text()').extract_first()

            # XPath expression to fetch author of the Quote
            authors = quote.xpath('.//*[@itemprop="author"]/text()').extract()

            # XPath expression to fetch Tags of the Quote
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()

            # Yield all elements
            yield {"Quote Text ": title, "Authors ": authors, "Tags ": tags}

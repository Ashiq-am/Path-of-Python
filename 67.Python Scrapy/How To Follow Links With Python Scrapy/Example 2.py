# Import the required libraries
import scrapy


# Spider class name


class GfgSpilinkSpider(scrapy.Spider):
    # Name of the spider
    name = 'gfg_spilink'

    # The domain to be scraped
    allowed_domains = ['quotes.toscrape.com']

    # The URLs to be scraped from the domain
    start_urls = ['http://quotes.toscrape.com/']

    # Default callback method
    def parse(self, response):
        # All quotes have CSS 'class 'attribute as 'quote'
        quotes = response.xpath('//*[@class="quote"]')

        # Loop through the quotes
        # selectors to fetch data for every quote
        for quote in quotes:
            # XPath expression to fetch
            # text of the Quote title
            # note the 'dot' operator since
            # we are extracting from single 'quote' element
            title = quote.xpath(
                './/*[@class="text"]/text()').extract_first()

            # XPath expression to fetch author of the Quote
            authors = quote.xpath('.//*[@itemprop="author"]/text()').extract()

            # XPath expression to fetch tags of the Quote
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()

            # Yield the data desired
            yield {"Quote Text ": title, "Authors ": authors, "Tags ": tags}

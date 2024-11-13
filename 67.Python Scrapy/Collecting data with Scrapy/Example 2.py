import scrapy

# importing the items structure described
# in items.py file
from ..items import ScrapytutorialItem


class SpiderToCrawlSpider(scrapy.Spider):
    name = 'spider_to_crawl'
    # allowed_domains = ['https://quotes.toscrape.com/']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # creating items dictionary
        items = ScrapytutorialItem()

        # this is selected by pressing ctrl+f in console
        # and selecting the appropriate rule of Xpath
        Quotes_all = response.xpath('//div/div/div/span[1]')

        # These paths are based on the selectors

        for quote in Quotes_all:  # extracting data
            items['Quote'] = quote.css('::text').extract()
            yield items
        # calling pipelines components for further
        # processing.

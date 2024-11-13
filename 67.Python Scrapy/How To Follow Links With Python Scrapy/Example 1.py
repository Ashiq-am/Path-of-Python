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
        pass

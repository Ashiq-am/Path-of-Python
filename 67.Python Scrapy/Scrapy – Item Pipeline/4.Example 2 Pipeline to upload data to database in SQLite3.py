import scrapy
from ..items import ScrapytutorialItem


class SpiderToCrawlSpider(scrapy.Spider):
    name = 'spider_to_crawl'

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # creating items dictionary
        items = ScrapytutorialItem()
        Quotes_all = response.xpath('//div/div/div/span[1]')

        # These paths are based on the selectors

        # extracting data
        for quote in Quotes_all:
            items['Quote'] = quote.css('::text').extract()
            yield items

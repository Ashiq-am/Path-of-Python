# Import the required Scrapy library
import scrapy


# The Spider class created
class LearnshellSpider(scrapy.Spider):
    # Name of spider mentioned in 'genspider'
    # command
    name = 'learnshell'

    # The domain to be scraped
    allowed_domains = ['quotes.toscrape.com/tag/friends/']

    # The allowed URLs to be scraped
    start_urls = ['http://quotes.toscrape.com/tag/friends/']

    # The default callback parse method
    def parse(self, response):
        pass

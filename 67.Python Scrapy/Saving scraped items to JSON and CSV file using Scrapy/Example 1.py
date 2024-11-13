# Import the required library
import scrapy


# Spider class
class GfgFriendquotesSpider(scrapy.Spider):
    # The name of the spider
    name = 'gfg_friendquotes'

    # The domain, the spider will crawl
    allowed_domains = ['quotes.toscrape.com/tag/friendship/']

    # The URL of the webpage, data from which
    # will get scraped
    start_urls = ['http://quotes.toscrape.com/tag/friendship/']

    # default start function which will hold
    # the code for navigating and gathering
    # the data from tags
    def parse(self, response):
        pass

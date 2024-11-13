# Import the required libraries
import scrapy

# Spider Class Created


class GfgSpiitemsreadSpider(scrapy.Spider):
	# Name of the spider
	name = 'gfg_spiitemsread'
	# The domain to be scraped
	allowed_domains = ['quotes.toscrape.com/tag/reading/']
	# The URLs from domain to scrape
	start_urls = ['http://quotes.toscrape.com/tag/reading//']

	# Spider default callback function
	def parse(self, response):
		pass

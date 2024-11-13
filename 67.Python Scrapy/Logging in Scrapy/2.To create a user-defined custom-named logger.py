import scrapy
import logging

logger = logging.getLogger('GFG_logger')

class LogSpider(scrapy.Spider):
	name = 'log'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	def parse(self, response):
		logger.info('Parse function called on %s', response.url)

import scrapy
import logging

logging.basicConfig(level=logging.CRITICAL,
					format='[%(asctime)s] {%(name)s} %(levelname)s: %(message)s',
					datefmt='%y-%m-%d %H:%M:%S')
logger = logging.getLogger('GFG_logger')

class LogSpider(scrapy.Spider):
	name = 'log'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	def parse(self, response):
		logger.info('Parse function called on %s', response.url)

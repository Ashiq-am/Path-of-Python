import scrapy

class LogSpider(scrapy.Spider):
	name = 'log'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	def parse(self, response):
		self.logger.info('Parse function called on %s', response.url)

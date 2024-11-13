import scrapy

class IntegratedspiderSpider(scrapy.Spider):
	name = 'integratedspider' # name of spider
	allowed_domains = ['example.com']
	start_urls = ['http://example.com/']

	def parse(self, response):
		pass

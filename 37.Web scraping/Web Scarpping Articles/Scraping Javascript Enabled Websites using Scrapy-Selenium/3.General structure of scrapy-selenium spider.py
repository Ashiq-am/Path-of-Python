import scrapy
from scrapy_selenium import SeleniumRequest

class IntegratedspiderSpider(scrapy.Spider):
	name = 'integratedspider'
	def start_requests(self):
		yield SeleniumRequest(
			url ="https://www.geeksforgeeks.org/",
			wait_time = 3,
			screenshot = True,
			callback = self.parse,
			dont_filter = True
		)

	def parse(self, response):
		pass

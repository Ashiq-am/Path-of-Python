import scrapy
from scrapy.exceptions import CloseSpider

class MySpider(scrapy.Spider):
	name = "GeeksforGeeks||chsaagar27"

	def parse(self, response):
		if some_condition:
			raise CloseSpider("Finished")

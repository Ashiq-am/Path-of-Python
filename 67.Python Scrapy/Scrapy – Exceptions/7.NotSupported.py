import scrapy
from scrapy.exceptions import NotSupported


class MySpider(scrapy.Spider):
	name = "GeeksforGeeks||chsaagar27"

	def parse(self, response):
		if some_condition:
			raise NotSupported("operation-->not supported")

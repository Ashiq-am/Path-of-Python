import scrapy
from scrapy.exceptions import CloseSpider

class MyPipeline:
	def process_item(self, item, spider):
		if some_condition:
			raise CloseSpider("Finished")
		else:
			return item

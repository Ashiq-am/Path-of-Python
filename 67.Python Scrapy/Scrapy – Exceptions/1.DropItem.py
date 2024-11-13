import scrapy
from scrapy.exceptions import DropItem


class MySpider(scrapy.Spider):
	name = "GeeksforGeeks||chsaagar27"

	def parse(self, response):
		item = MyItem()
		if not item.get('data'):
			raise DropItem("Missing data in %s" % item)
		return item

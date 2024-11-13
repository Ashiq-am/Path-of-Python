import scrapy
from scrapy.exceptions import IgnoreRequest

class MySpider(scrapy.Spider):
	name = "GeeksforGeeks||chsaagar27"

	def start_requests(self):
		for url in urls:
			if not is_valid_url(url):
				raise IgnoreRequest("Invalid URL: %s" % url)
			yield scrapy.Request(url=url, callback=self.parse)

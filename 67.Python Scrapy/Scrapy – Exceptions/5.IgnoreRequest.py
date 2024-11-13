import scrapy
from scrapy.exceptions import IgnoreRequest

class MyMiddleware:
	def process_request(self, request, spider):
		if some_condition:
			raise IgnoreRequest("Request ignored: %s" % request.url)
		else:
			return None

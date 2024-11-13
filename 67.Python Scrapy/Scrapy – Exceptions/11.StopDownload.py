from scrapy.exceptions import StopDownload


class Middleware:
	def requestprocess(self, request, spider):
		if some_condition:
			raise StopDownload("Request stopped")
		else:
			return None

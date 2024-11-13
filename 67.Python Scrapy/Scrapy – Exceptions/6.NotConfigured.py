import scrapy
from scrapy.exceptions import NotConfigured

class MyExtension:

	def from_crawler(cls, crawler):
		setting1 = crawler.settings.get('SETTING_1')
		setting2 = crawler.settings.get('SETTING_2')

		if not setting1 or not setting2:
			raise NotConfigured("SETTING_1 and \
						SETTING_2 must be set")

		return cls(setting1, setting2)

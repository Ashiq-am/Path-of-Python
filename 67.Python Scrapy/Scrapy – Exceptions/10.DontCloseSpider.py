from scrapy.exceptions import DontCloseSpider
from scrapy.spiders import Spider

class MySpider(Spider):
    name = 'Geeks for Geeks || chsaagar27'

    def parse(self, response):
        # process
        def close_spider(self, spider):
            raise DontCloseSpider

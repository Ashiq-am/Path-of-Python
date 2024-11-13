# import section
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GFGSpidey(CrawlSpider):
	name = "gfg_spidey"
	# list of URLs to scrape
	allowed_domains = ["geeksforgeeks.org"]
	start_urls = ["https://www.geeksforgeeks.org/category/c-arrays/"]
	# creation of rules
	rules = (
		Rule(LinkExtractor(allow="c-arrays"), callback="parse_item"),
	)
	# method to parse

	def parse_item(self, response):
		# saving items via yield dictionary
		yield{
			"Title of article": response.css("div.head a::text").get(),
			"Tag present": response.css("div.item a::text").get()
		}

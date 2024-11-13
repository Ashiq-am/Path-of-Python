# booklist\spiders\book.py

import scrapy
from booklist.items import BooklistItem

class BookSpider(scrapy.Spider):
	name = 'book'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	# To store in JSON format
	custom_settings = {
		'FEEDS': {'data.json': {'format': 'json', 'overwrite': True}}
	}

	def parse(self, response):
		for article in response.css('article.product_pod'):
			book_item = BooklistItem(
				url=article.css("h3 > a::attr(href)").get(),
				title=article.css("h3 > a::attr(title)").extract_first(),
				price=article.css(".price_color::text").extract_first(),
			)
			yield book_item

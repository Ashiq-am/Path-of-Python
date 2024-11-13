import scrapy


class python_Spider(scrapy.Spider):
    name = "geeksforgeeks_article"

    start_urls = [
        'https://www.geeksforgeeks.org/data-structures/?ref=shm',
    ]

    #def parse(self, response):


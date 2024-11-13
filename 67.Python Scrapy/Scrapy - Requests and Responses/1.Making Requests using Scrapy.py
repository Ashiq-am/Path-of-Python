# performing a scrapy request to get the data from the website
import scrapy


class MySpider(scrapy.Spider):
    name = 'scrapy_example'

    def start_requests(self):
        yield scrapy.Request(url='http://www.example.com', callback=self.parse)

    def parse(self, response):
        # Process the response here

        print(response.body)

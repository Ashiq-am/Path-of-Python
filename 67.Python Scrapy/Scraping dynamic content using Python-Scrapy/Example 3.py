import scrapy


class python_Spider(scrapy.Spider):
    name = "python_events"

    start_urls = [
        'https://www.python.org/blogs/',
    ]

    def parse(self, response):
        for item in response.css('ol'):
            yield {
                'title': item.css('a::text').get(),
                'link': item.css('a::attr(href)').get(),
            }

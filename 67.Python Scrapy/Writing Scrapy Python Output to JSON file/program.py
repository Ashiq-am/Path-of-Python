import scrapy


class QuotesSpider(scrapy.Spider):
    # name of variable should be 'name' only
    name = "quotes"

    # urls from which will be used to extract information
    # list should be named 'start_urls' only
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        # handle the response downloaded for each of the
        # requests made should be named 'parse' only
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

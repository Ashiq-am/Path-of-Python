# Import the required libraries
import scrapy


# The Spider code
class LearnshellSpider(scrapy.Spider):
    # Name of the spider
    name = 'learnshell'

    # The domain allowed for scraping
    allowed_domains = ['quotes.toscrape.com/tag/friends']

    # The URL(s) to be scraped
    start_urls = ['http://quotes.toscrape.com/tag/friends/']

    # Default callback method called when a spider crawls
    def parse(self, response):
        if "quotes" in response.url:
            # Invoke the Scrapy Shell and inspect the response
            from scrapy.shell import inspect_response

            # Inspect the response
            inspect_response(response, self)

            # Execute rest of the code after
            # inspecting the response at shell and exit()
            # XPath selector for fetching the author names
            quotes = response.xpath('//*[@class="author"]/text()').extract()

            # The spider crawls and prints the authors
            # present on the URL
            yield {'Authors': quotes}

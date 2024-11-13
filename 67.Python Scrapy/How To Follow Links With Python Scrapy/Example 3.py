# Import the required libraries
import scrapy


# Spider class name
class GfgSpilinkSpider(scrapy.Spider):
    # Name of the spider
    name = 'gfg_spilink'

    # The domain to be scraped
    allowed_domains = ['quotes.toscrape.com']

    # The URLs to be scraped from the domain
    start_urls = ['http://quotes.toscrape.com/']

    # Default callback method
    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            # XPath expression to fetch
            # text of the Quote title
            title = quote.xpath('.//*[@class="text"]/text()').extract_first()

            # XPath expression to fetch
            # author of the Quote
            authors = quote.xpath('.//*[@itemprop="author"]/text()').extract()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()
            yield {"Quote Text ": title, "Authors ": authors, "Tags ": tags}

        # Check CSS attribute of the "Next"
        # hyperlink and extract its "href" value
        further_page_url = response.xpath(
            '//*[@class="next"]/a/@href').extract_first()

        # Append the "href" value, to the current page,
        # to form a complete URL, of next page
        complete_url_next_page = response.urljoin(further_page_url)

        # Make the spider crawl, to the next page,
        # and extract the same data
        # A new Request with the URL is made
        yield scrapy.Request(complete_url_next_page)

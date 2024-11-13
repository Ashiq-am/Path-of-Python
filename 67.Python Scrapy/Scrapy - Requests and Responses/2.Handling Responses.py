import scrapy


class MySpider(scrapy.Spider):
    name = 'scrapy_example'

    def start_requests(self):
        yield scrapy.Request(url='http://www.example.com',
                             callback=self.parse)

    def parse(self, response):
        # Extract data from the response from all h1 and p tags
        headings = response.css('h1::text').getall()
        paragraphs = response.css('p::text').getall()

        # Print the extracted data
        print("Headings:")
        for heading in headings:
            print(heading)

        print("\nParagraphs:")
        for paragraph in paragraphs:
            print(paragraph)

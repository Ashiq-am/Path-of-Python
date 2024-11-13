# Parse function
def parse(self, response):
    # Extra feature to get title
    title = response.css('title::text').extract_first()

    # Get anchor tags
    links = response.css('a::attr(href)').extract()

    for link in links:
        yield
        {
            'title': title,
            'links': link
        }

        if 'geeksforgeeks' in link:
            yield scrapy.Request(url=link, callback=self.parse)

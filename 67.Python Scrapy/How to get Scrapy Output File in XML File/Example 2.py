def parse(self, response):
    countries = response.xpath("//tr")

    for country in countries:
        name = country.xpath("(.//td)[2]/a/text()").get()
        population = country.xpath("(.//td)[3]/text()").get()
        yield {
            'name': name,
            'population': population

        }

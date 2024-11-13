# Spider dedicated to GeekForGeeks

# Importing necessary packages
import scrapy

# Creating the spider class


class GFGSpider (scrapy.Spider):
	# Assigning a name to the created spider
	name = "gfg"

	# Defining start_requests() function
	def start_requests(self):
		url_list = [""]	 # Enter your target URL here
		for url in url_list:
			yield scrapy.Request(url=url, callback=self.parse)

	# Defining parse() function
	def parse(self, response):
		page = response.url.split("/")[-2]
		file_name = "gfg-%s.html" % page # Name of the output file
		with open(file_name, 'wb') as file:
			file.write(response.body) # Writing the file
		self.log("file saved %s" % file_name)

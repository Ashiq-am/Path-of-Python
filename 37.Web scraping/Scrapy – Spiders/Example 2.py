# import section
import scrapy

# spider inheriting Spider base class


class GFGImageSpider (scrapy. Spider):
	name = "gfg_img"
	start_urls = ["https://practice.geeksforgeeks.org/"]

	def parse(self, response):
		# using xpath selector
		links = response.xpath("//img/@src")
		# to store html content in the form of string
		html = ""

		for link in links:
			# converting link to string
			url = link.get()
			# checking for images
			if any(extension in url for extension in [".jpg",
													".gif",
													".png"]):
				html += """<a href="{url}"
				target="_blank">
				<img src="{url}" height="33%"
				width="33%" />
				<a/>""". format(url=url)
				# creating a file to write html content
				with open("gfg_images.html", "a") as page:
					page.write(html)
					page.close()

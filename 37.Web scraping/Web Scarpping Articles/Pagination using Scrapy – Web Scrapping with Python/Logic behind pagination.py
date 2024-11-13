"""

"""

"""

next_page = response.xpath("//div/div/ul/li[@class='alast']/a/@href").get() 
if next_page: 
	abs_url = f"https://www.amazon.in{next_page}"
yield scrapy.Request( 
	url=abs_url, 
	callback=self.parse 
) 




"""
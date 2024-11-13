# Create loader object
loader = ItemLoader(item=Item())

# Item loader method for phoneno,
# mention the field name and xpath expression
loader.add_xpath('phoneno',
				'//footer/a[@class = "phoneno"]/@href')

# Item loader method for map,
# mention the field name and xpath expression
loader.add_xpath('map',
				'//footer/a[@class = "map"]/@href')

# populate the item
loader.load_item()

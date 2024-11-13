# Define Item Loader object by passing item
loader = ItemLoader(item=Item())

# Create nested loader with footer selector
footer_loader = loader.nested_xpath('//footer')

# Add phoneno xpath values relative to the footer
footer_loader.add_xpath('phoneno', 'a[@class = "phoneno"]/@href')

# Add map xpath values relative to the footer
footer_loader.add_xpath('map', 'a[@class = "map"]/@href')

# Call loader.load_item() to populate values
loader.load_item()

# soup.find.all( h3 ) to grab
# all major headings of our search result,
heading_object=soup.find_all( 'h3' )

# Iterate through the object
# and print it as a string.
for info in heading_object:
	print(info.getText())
	print("------")

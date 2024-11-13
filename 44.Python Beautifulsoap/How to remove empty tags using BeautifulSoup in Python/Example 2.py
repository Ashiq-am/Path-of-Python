# Import Module
from bs4 import BeautifulSoup
import requests

# Page URL
URL = "https://www.geeksforgeeks.org/"

# Page content from Website URL
page = requests.get( URL )

# Get HTML Code
soup = BeautifulSoup( page.content , "lxml" )

# Iterate each line
for x in soup.find_all():

	# fetching text from tag and remove whitespaces
	if len( x.get_text ( strip = True )) == 0:

		# Remove empty tag
		x.extract()

# Print HTML Code with removed empty tags
print(soup)

# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with an HTML page
soup = BeautifulSoup('''
	<html>
		<h1>a web page</h1>
	</html>
	''', "lxml")

# Get the tag
tag = soup.h1

# Print the output
print(tag)

# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with an HTML page
soup = BeautifulSoup('''
	<html>
		<strong>a web page</strong>
	</html>
	''', "lxml")

# Get the tag
tag = soup.strong

# Print the output
print(type(tag))

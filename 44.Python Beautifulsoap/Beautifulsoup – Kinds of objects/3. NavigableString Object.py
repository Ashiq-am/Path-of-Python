# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with an HTML page
soup = BeautifulSoup('''
	<html>
		<b>Geeks for Geeks</b>
	</html>
	''', "html.parser")

# Get the tag
tag = soup.b

# Get the string inside the tag
string = tag.string

# Print the output
print(type(string))

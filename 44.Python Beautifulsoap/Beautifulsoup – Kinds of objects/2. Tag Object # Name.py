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

# Print the output
print(tag.name)

# changinf the tag
tag.name = "Strong"
print(tag)

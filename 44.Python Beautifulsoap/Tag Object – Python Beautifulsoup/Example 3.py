# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with a HTML page
soup = BeautifulSoup('''
	<html>
		<strong>the first strong tag</strong>
		<h1> Heading </h1>
		<strong>the second strong tag</strong>
	</html>
	''', "lxml")

# Get the tag
tag = soup.strong

# Print the output
print(tag)

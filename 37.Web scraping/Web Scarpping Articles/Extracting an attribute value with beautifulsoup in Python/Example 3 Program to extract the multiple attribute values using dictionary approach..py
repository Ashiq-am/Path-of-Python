# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with a HTML page
soup = BeautifulSoup(''' 
	<html> 
		<h2 class="first second third"> Heading 1 </h2> 
		<h1> Heading 2 </h1> 
	</html> 
	''', "lxml")

# Get the whole h2 tag
tag = soup.h2

# Get the attribute
attribute = tag['class']

# Print the output
print(attribute)

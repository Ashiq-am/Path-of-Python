# Import module
from bs4 import BeautifulSoup

# Initialize the object with a XML
soup = BeautifulSoup(''' 
	<root> 
		<name_of_tag>the first strong tag</name_of_tag> 
	</root> 
	''', "lxml")

# Get the tag
tag = soup.name_of_tag

# Get the tag name
name = tag.name

# Print the output
print(name)

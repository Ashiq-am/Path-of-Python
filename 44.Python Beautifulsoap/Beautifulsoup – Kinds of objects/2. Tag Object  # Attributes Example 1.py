# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with an HTML page
soup = BeautifulSoup('''
	<html>
		<b class="gfg">Geeks for Geeks</b>
	</html>
	''', "html.parser")

# Get the tag
tag = soup.b

print(tag["class"])

# modifing class
tag["class"] = "geeks"
print(tag)

# delete the class attrbutes
del tag["class"]
print(tag)

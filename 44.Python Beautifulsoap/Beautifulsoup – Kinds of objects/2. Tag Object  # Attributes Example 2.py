# Import Beautiful Soup
from bs4 import BeautifulSoup

# Initialize the object with an HTML page
# soup for multi_valued attributes
soup = BeautifulSoup('''
	<html>
		<b class="gfg geeks">Geeks for Geeks</b>
	</html>
	''', "html.parser")

# Get the tag
tag = soup.b

print(tag["class"])

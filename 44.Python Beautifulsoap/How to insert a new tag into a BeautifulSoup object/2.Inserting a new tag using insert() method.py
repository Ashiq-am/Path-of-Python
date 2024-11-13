# Import Module
from bs4 import BeautifulSoup

# HTML Document
HTML_DOC = """
			<html>
			<head>
				<title> Add new Tag </title>
			</head>
			<body>
					<div> This is sample div 1 </div>
					<div> This is sample div 2 </div>
			</body>
			</html>
			"""

# Function to inset new tag
def addTag(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	# create new tag
	# Here we are creating a new div
	new_div = soup.new_tag("div")

	# Adding content to div
	new_div.string = " This is new div "

	# Inserting new div to html tree
	# Here, 2 represents the position
	# where we want to insert the new tag
	soup.html.body.insert(2, new_div)

	# Printing the modified object
	print(soup)


# Function Call
addTag(HTML_DOC)

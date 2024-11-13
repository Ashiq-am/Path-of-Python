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

# Function to insert new tag after given tag
def addTag(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	# create new tag
	# Here we are creating a new div
	new_div_after = soup.new_tag("div")

	# Adding content to div
	new_div_after.string = " This is new div after div 1 "

	# Inserting new tag after div 1
	soup.html.body.div.insert_after(new_div_after)

	# Printing the modified object
	print(soup)


# Function Call
addTag(HTML_DOC)

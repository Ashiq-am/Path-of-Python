# Import Module
from bs4 import BeautifulSoup

# HTML Document
HTML_DOC = """
			<html>
			<head>
				<title> Geeksforgeeks </title>
			</head>
			<body>
				<div class="ext" >Extract this tag</div>
			</body>
			</html>
			"""

# Function to find tags
def find_tags_from_class(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	# find tags by CSS class
	div = soup.find("div", class_= "ext")

	# Print the extracted tag
	print(div)

# Function Call
find_tags_from_class(HTML_DOC)

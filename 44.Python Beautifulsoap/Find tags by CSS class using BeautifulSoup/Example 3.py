# Import Module
from bs4 import BeautifulSoup
import re

# HTML Document
HTML_DOC = """
			<html>
			<head>
				<title> Table Data </title>
			</head>
			<body>
				<table>
				<tr>
					<td class = "table"> This is row 1 </td>
					<td class = "table-row"> This is row 2 </td>
					<td class = "table"> This is row 3 </td>
					<td class = "table-row"> This is row 4 </td>
					<td class = "table"> This is row 5 </td>
				</tr>
				</table>
			</body>
			</html>
			"""

# Function to find tags
def find_tags_from_class(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	# find tags by CSS class using regular expressions
	# $ is used to match pattern ending with
	# Here we are finding class that ends with "row"
	rows = soup.find_all("td", class_= re.compile("row$"))

	# Print the extracted tag
	for row in rows:
		print(row)

# Function Call
find_tags_from_class(HTML_DOC)

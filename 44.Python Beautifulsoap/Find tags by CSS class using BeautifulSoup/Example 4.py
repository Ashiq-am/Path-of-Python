# Import Module
from bs4 import BeautifulSoup

# HTML Document
HTML_DOC = """
			<html>
			<head>
				<title> Table Data </title>
			</head>
			<body>
				<table>
				<tr>
					<td class = "table"> This is invalid because len(table) != 3 </td>
					<td class = "row"> This is valid because len(row) == 3 </td>
					<td class = "data"> This is invalid because len(data) != 3 </td>
					<td class = "hii"> This is valid because len(hii) == 3 </td>
					<td> This is invalid because class is None </td>
				</tr>
				</table>
			</body>
			</html>
			"""

# Returns true if the css_class is not None
# and length of css_class is equal to 3
# else returns false
def has_three_characters(css_class):
	return css_class is not None and len(css_class) == 3


# Function to find tags
def find_tags_from_class(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	# find tags by CSS class using user-defined function
	rows = soup.find_all("td", class_= has_three_characters)

	# Print the extracted tag
	for row in rows:
		print(row)

# Function Call
find_tags_from_class(HTML_DOC)

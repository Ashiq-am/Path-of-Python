# import BeautifulSoup
from bs4 import BeautifulSoup

# create html document
html = """
	<html>
			<head>
				<title> Hi I am Title </title>
			</head>
	<body>

<p>	 GFG BeautifulSoup tutorial
			</p>

	</body>
	</html>
"""

# invoke BeautifulSoup()
soup = BeautifulSoup(html, 'html.parser')
print(" *** Title of the document *** ")

# invoke find()
print(soup.find("title"))

# import module
from bs4 import BeautifulSoup

# assign HTML document
html_doc = """
<html>

<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page to find the length of
the first tag</title>
</head>

<body>
<h2>An example of HTML page to find the length of the
first tag</h2>

<p>
Beautiful Soup is a library which is essential to scrape
information from web pages.
It helps to iterate, search and modifying the parse tree.</p>

</body>
</html>
"""

# create beautiful soap object
soup = BeautifulSoup(html_doc, 'html.parser')

# assign tag
tag = "html"

# get length
print("Length of the text of", tag, "tag is:",
	len(soupResults.find(tag).text))

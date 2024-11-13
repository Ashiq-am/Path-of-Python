# Import Module
from bs4 import BeautifulSoup

# HTML CODE
html_code = """<a><b>text1</b><d>text3</d><c>text2</c></a>"""

# Parse HTML CODE
soup = BeautifulSoup(html_code, 'html.parser')

# previous element
for element in soup.c.previous_siblings:
	print(element)

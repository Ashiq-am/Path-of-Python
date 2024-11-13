# Import Module
from bs4 import BeautifulSoup

# HTML CODE
html_code = """<a><b>text1</b><c>text2</c></a>"""

# Parse HTML CODE
soup = BeautifulSoup(html_code, 'html.parser')

# previous element
print(soup.c.previous_sibling)

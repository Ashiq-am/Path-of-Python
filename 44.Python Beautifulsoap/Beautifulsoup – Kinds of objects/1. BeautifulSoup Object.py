# importing the module
from bs4 import BeautifulSoup

# parsing the document
soup = BeautifulSoup('''<h1>Geeks for Geeks</h1>''',
					"html.parser")

print(type(soup))

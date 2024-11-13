# importing module
from bs4 import BeautifulSoup

markup = '''<html><body><div id="container">Div Content</div></body></html>'''
soup = BeautifulSoup(markup, 'html.parser')

# finding the tag with the id attribute
div_bs4 = soup.find(id="container")

print(div_bs4.name)

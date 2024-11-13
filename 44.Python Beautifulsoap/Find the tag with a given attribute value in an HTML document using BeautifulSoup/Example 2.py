# importing module
from bs4 import BeautifulSoup

markup = '''<html><body><a href="https://www.geeksforgeeks.org/">Geeks for Geeks</a></body></html>'''
soup = BeautifulSoup(markup, 'html.parser')

# finding the tag with the href attribute
div_bs4 = soup.find(href="https://www.geeksforgeeks.org/")

print(div_bs4.name)

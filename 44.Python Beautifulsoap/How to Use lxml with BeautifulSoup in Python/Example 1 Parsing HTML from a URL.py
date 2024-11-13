from bs4 import BeautifulSoup
import requests
from lxml import etree

url = 'https://geeksforgeeks.org'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
title = soup.title.string

print(f"Title of the webpage: {title}")

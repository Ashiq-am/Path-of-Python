from bs4 import BeautifulSoup
import requests

# sample web page
sample_web_page = 'https://www.geeksforgeeks.org/caching-page-tables/'

# call get method to request that page
page = requests.get(sample_web_page)

# with the help of beautifulSoup and html parser create soup
soup = BeautifulSoup(page.content, "html.parser")

text = 'CS Theory Course'

# Search by text with the help of lambda function
gfg = soup.find_all(lambda tag: tag.name == "strong" and text in tag.text)

print(gfg)

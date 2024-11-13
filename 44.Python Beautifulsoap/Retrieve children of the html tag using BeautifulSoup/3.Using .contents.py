from bs4 import BeautifulSoup
import requests

# sample web page
sample_web_page = 'https://www.geeksforgeeks.org/caching-page-tables/'

# call get method to request that page
page = requests.get(sample_web_page)

# with the help of beautifulSoup and html parser create soup
soup = BeautifulSoup(page.content, "html.parser")

child_soup = soup.find('p')

print("child : ", child_soup.contents)

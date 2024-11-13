from bs4 import BeautifulSoup
import requests

# sample web page
sample_web_page = 'https://www.geeksforgeeks.org/caching-page-tables/'

# call get method to request that page
page = requests.get(sample_web_page)

# with the help of beautifulSoup and html parser create soup
soup = BeautifulSoup(page.content, "html.parser")

child_soup = soup.find_all('strong')

text = 'page table base register (PTBR)'

# we will search the tag with in which text is same as given text
for i in child_soup:
	if(i.string == text):
		print(i)

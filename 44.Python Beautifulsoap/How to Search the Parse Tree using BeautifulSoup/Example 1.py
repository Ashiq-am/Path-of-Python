from bs4 import BeautifulSoup
import requests


# sample website
sample_website = 'https://www.geeksforgeeks.org/difference-between-article-and-blog/'

# call get method to request the page
page = requests.get(sample_website)

# with the help of BeautifulSoup method and
# html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

# With the help of find method perform searching
# in parser tree
print(soup.find('th'))

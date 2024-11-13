from bs4 import BeautifulSoup
import requests

# sample website
sample_website = 'https://www.geeksforgeeks.org/different-ways-to-remove-all-the-digits-from-string-in-java/'

# call get method to request the page
page = requests.get(sample_website)

# with the help of BeautifulSoup method and html
# parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

# With the help of . operater we will scrap a tag
# under body->a
# here we will go a tag inside body then a then
# li.means under the body tag we will go to a tag
print(soup.body.a)

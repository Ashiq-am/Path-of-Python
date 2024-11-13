from bs4 import BeautifulSoup
import requests

# sample website
sample_website = 'https://www.geeksforgeeks.org/different-ways-to-remove-all-the-digits-from-string-in-java/'

# call get method to request the page
page = requests.get(sample_website)

# with the help of BeautifulSoup method and
# html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

# With the help of . operater we will scrap a tag
# under body->ui->i
# here we will go a tag inside body then ul then
# i.means under the body tag we will go to ul tag
# and again inside the ul tag we will go i tag
print(soup.body.ul.i)

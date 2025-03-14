from bs4 import BeautifulSoup
import requests

# sample website
sample_website = 'https://www.geeksforgeeks.org/different-ways-to-remove-all-the-digits-from-string-in-java/'

# call get method to request the page
page = requests.get(sample_website)

# with the help of BeautifulSoup
# method and html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

# With the help of find_all
# method perform searching in parser tree
for i in soup.find_all('a', href=True):

    # check all link which is contain
    # "www.geeksforgeeks.org" string
    if ("www.geeksforgeeks.org" in i['href']):
        # call get method to request next url
        nextpage = requests.get(i['href'])

        # create soup for next url
        nextsoup = BeautifulSoup(nextpage.content, 'html.parser')

        # we can scrap any thing of the
        # next page here we are scraping title of
        # nexturl page string
        print("next url title : ", nextsoup.find('title').string)

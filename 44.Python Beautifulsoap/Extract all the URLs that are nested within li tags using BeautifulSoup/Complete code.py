# Importing libraries
import requests
from bs4 import BeautifulSoup

# setting up the URL
URL = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'

# perform get request to the url
reqs = requests.get(URL)

# extract all the text that you received from
# the GET request
content = reqs.text

# convert the text to a beautiful soup object
soup = BeautifulSoup(content, 'html.parser')

# Empty list to store the output
urls = []

# For loop that iterates over all the <li> tags
for h in soup.findAll('li'):

    # looking for anchor tag inside the <li>tag
    a = h.find('a')
    try:

        # looking for href inside anchor tag
        if 'href' in a.attrs:
            # storing the value of href in a separate variable
            url = a.get('href')

            # appending the url to the output list
            urls.append(url)

    # if the list does not has a anchor tag or an anchor tag
    # does not has a href params we pass
    except:
        pass

# print all the urls stored in the urls list
for url in urls:
    print(url)

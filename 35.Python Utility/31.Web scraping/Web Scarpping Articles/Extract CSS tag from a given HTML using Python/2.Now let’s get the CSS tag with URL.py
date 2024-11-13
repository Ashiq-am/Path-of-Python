# import module
from bs4 import BeautifulSoup
import requests


# link for extract html data
# Making a GET request

def getdata(url):
    r = requests.get(url)
    return r.text


html_doc = getdata('https://www.geeksforgeeks.org/')
soup = BeautifulSoup(html_doc, "lxml")

# traverse CSS from soup

print("\nTags by CSS class:")
print(soup.select(".header-main__wrapper"))

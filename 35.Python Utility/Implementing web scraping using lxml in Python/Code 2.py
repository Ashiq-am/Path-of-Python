import requests
from lxml import html

# url to scrape data from
link = 'https://en.wikipedia.org / wiki / Web_scraping'

# path to particular element
path = '//*[@id ="mw-content-text"]/div / p[1]'

response = requests.get(link)
byte_string = response.content

# get filtered source code
source_code = html.fromstring(byte_string)

# jump to preferred html element
tree = source_code.xpath(path)

# print texts in first element in list
print(tree[0].text_content())

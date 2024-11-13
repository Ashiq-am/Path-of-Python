# import module
import requests
from bs4 import BeautifulSoup

# link for extract html data
# Making a GET request
def getdata(url):
	r = requests.get(url)
	return r.text


# input by geek
# MICR code
Micr = "800002012"

# url
url = "https://micr.bankifsccode.com/"+Micr


# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# traverse the bank information
data = []
for i in (soup.find_all("div", class_="text6")):
	data.append((i.get_text()))

# Validate the
# data
if len(data) == 0:
	print("Not Valid MICR Code")
else:
	print("Found")
	print(data)

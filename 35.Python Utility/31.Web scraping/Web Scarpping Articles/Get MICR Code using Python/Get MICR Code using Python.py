# import module
import requests
from bs4 import BeautifulSoup

# link for extract html data
# Making a GET request
def getdata(url):
	r = requests.get(url)
	return r.text


# input by geek
# bank details
bank_name = "KOTAK_MAHINDRA_BANK"
state = "BIHAR"
city = "PATNA"
branch = "PATNA"

# url
url = "https://bankifsccode.com/"+bank_name+"/"+state+"/"+city+"/"+branch


# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# traverse the data
data = []
for i in (soup.find_all('a')):
	data.append((i.get_text()))

print("MICR Code :")
print(data[17])

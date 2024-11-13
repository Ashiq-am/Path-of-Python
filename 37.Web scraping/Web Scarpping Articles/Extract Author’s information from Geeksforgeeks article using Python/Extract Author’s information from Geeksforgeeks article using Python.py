# import module
import requests
from bs4 import BeautifulSoup

# link for extract html data
# Making a GET request


def getdata(url):
	r = requests.get(url)
	return r.text


# input article by geek
article = "optparse-module-in-python"

# url
url = "https://www.geeksforgeeks.org/"+article


# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# traverse auther name
for i in soup.find('div', class_="author_handle"):
	Author = i.get_text()

# now get auther infromation
# with auther name
profile = 'https://auth.geeksforgeeks.org/user/'+Author+'/profile'

# pass the url
# into getdata function
htmldata = getdata(profile)
soup = BeautifulSoup(htmldata, 'html.parser')

# traverse information of auther
name = soup.find(
	'div', class_='mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold medText').get_text()


author_info = []
for item in soup.find_all('div', class_='mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold'):
	author_info.append(item.get_text())

print("Author name :", name)
print("Author information :")
print(author_info)

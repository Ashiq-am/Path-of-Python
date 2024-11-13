# input article by geek
article = "optparse-module-in-python"

# url
url = "https://www.geeksforgeeks.org/"+article

# pass the url
# into getdata function
htmldata=getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# display html code
print(soup)

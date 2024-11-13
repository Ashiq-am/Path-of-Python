# input by geek
station = "new-delhi"

# url
url = "https://www.mapsofindia.com/railways/station-code/"+station+".html"

# pass the url
# into getdata function
htmldata=getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# display html code
print(soup)

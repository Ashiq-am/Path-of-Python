# input by geek
train_name = "03391-rajgir-new-delhi-clone-special-rgd-to-ndls"

# url
url = "https://www.railyatri.in/live-train-status/"+train_name

# pass the url
# into getdata function
htmldata=getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# display html code
print(soup)

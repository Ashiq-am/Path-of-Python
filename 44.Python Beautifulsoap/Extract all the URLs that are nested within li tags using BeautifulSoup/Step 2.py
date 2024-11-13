# perform get request to the url
reqs = requests.get(URL)

# extract all the text that you received
# from the GET request
content = reqs.text

# convert the text to a beautiful soup object
soup = BeautifulSoup(content, 'html.parser')

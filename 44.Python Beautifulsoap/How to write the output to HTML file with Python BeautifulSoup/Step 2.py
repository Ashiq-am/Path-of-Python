# set the url to perform the get request
URL = 'https://www.geeksforgeeks.org/how-to-scrape-all-pdf-files-in-a-website/'
page = requests.get(URL)

# load the page content
text = page.content

# make a soup object by using beautiful
# soup and set the markup as html parser
soup = BeautifulSoup(text, "html.parser")

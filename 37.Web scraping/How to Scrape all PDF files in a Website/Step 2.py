# website to scrap
url = "https://www.rgpvonline.com/rgpv-first-year.html"

# get the url from requests get method
read = requests.get(url)

# full html content
html_content = read.content

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")

url = "https://www.reddit.com/r/learnpython/comments/78qnze/web_scraping_in_20_lines_of_code_with/"

# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# display html code
print(soup)

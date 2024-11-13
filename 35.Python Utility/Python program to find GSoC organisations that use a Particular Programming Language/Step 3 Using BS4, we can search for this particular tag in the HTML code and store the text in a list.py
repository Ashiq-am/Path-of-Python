# Specify the language you
# want to search for
language = 'python'

# BS4 object to store the
# html text We use res.text
# to get the html code in text format
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Selecting the specific tag
# with class name
orgElem = soup.select('h4[class ="organization-card__name font-black-54"]')


# Similarly finding the links
# for each org's gsoc page
orgLink = soup.find_all("a", class_="organization-card__link")
languageCheck = ['no'] * len(orgElem)
orgURL = ['none'] * len(orgElem)

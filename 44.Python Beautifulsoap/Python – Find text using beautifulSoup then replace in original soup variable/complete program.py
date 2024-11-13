import bs4
from bs4 import BeautifulSoup
import requests


# sending a GET requests
response = requests.get("https://isitchristmas.today/")

# a status 200 implies a sucessfull requests
#print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

title = soup.find("title")
heading = soup.find("h1")

# replacde
title.string = "Is GFG day today?"
heading.string = "Welcome to GFG"

# display replaced content
print(soup)
# The title and the heading tag contents
# get changed in the parsed soup obj.

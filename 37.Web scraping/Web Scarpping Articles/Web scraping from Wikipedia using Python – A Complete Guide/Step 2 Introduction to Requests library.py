# import required modules
import requests

# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# display status code
print(page.status_code)

# display scrapped data
print(page.content)

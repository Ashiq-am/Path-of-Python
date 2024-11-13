import bs4
from bs4 import BeautifulSoup
import requests

# sending a GET req.
response = requests.get("https://isitchristmas.today/")
print(response.status_code)

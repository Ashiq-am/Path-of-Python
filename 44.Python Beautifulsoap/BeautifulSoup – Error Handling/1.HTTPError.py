# importing modules
import requests
from urllib.error import HTTPError

url = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'

try:
    response = requests.get(url)

except HTTPError as hp:
    print(hp)

else:
    print("it's worked")

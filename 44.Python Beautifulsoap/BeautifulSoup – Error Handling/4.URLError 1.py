# importing modules
import requests
from urllib.error import URLError

url = 'https://www.geeksforgeks.org/implementing-web-scraping-python-beautiful-soup/'

try:
	response = requests.get(url)

except URLError as ue:
	print("The Server Could Not be Found")

else:
	print("No Error")

# code
import requests

url = "https://www.amazon.com/nothing_here"

try:
	r = requests.get(url, timeout=1)
	r.raise_for_status()
except requests.exceptions.HTTPError as errh:
	print("HTTP Error")
	print(errh.args[0])
# Prints the response code
print(r)

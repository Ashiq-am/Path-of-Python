import requests

url = "https://www.google.com"
# code
try:
	r = requests.get(url, timeout=1)
	r.raise_for_status()
except requests.exceptions.ReadTimeout as errrt:
	print("Time out")

print(r)

url = "https://www.google.com"
# code
try:
	r = requests.get(url, timeout=1)
	r.raise_for_status()
except requests.exceptions.RequestException as errex:
	print("Exception request")

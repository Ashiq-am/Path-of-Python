# import module
from urllib.request import urlopen, URLError, HTTPError

# exception handling to
# catch URL error
try:
	html = urlopen("https://www.geeksforgeeks.org/")

except URLError as e:
	print("Server not found!")

except HTTPError as e:
	print("HTTP error")

else:
	print("Server found")

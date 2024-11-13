# Import the required Modules
import requests

# Create a pool of proxies
proxies = {
	'http://114.121.248.251:8080',
	'http://222.85.190.32:8090',
	'http://47.107.128.69:888',
	'http://41.65.146.38:8080',
	'http://190.63.184.11:8080',
	'http://45.7.135.34:999',
	'http://141.94.104.25:8080',
	'http://222.74.202.229:8080',
	'http://141.94.106.43:8080',
	'http://191.101.39.96:80'
}

url = 'https://ipecho.net/plain'

# Iterate the proxies and check if it is working.
for proxy in proxies:
	try:

		# https://ipecho.net/plain returns the ip address
		# of the current session if a GET request is sent.
		page = requests.get(
		url, proxies={"http": proxy, "https": proxy})

		# Prints Proxy server IP address if proxy is alive.
		print("Status OK, Output:", page.text)

	except OSError as e:

		# Proxy returns Connection error
		print(e)

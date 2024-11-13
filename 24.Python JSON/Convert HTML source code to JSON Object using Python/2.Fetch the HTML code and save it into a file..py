# Sample URL to fetch the html page
url = "https://geeksforgeeks-example.surge.sh"

# Headers to mimic the browser
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Get the page through get() method
html_response = requests.get(url=url, headers = headers)

# Save the page content as sample.html
with open("sample.html", "w") as html_file:
	html_file.write(html_response.text)

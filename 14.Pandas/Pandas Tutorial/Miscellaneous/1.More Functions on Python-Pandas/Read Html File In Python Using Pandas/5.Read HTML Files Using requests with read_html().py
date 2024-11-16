import pandas as pd
import requests

def read_html_with_requests(file_url):
	# Fetch HTML content using requests
	response = requests.get(file_url)
	# Read HTML content into DataFrame using read_html()
	df = pd.read_html(response.content)[0]
	return df

# File URL
html_file_url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240213175028/geeks_for_geeks.html'

# Read HTML file using requests with read_html()
df = read_html_with_requests(html_file_url)

# Display DataFrame
print("Approach 3 Output:")
print(df)

import pandas as pd
from bs4 import BeautifulSoup

def read_html_with_beautiful_soup(file_path):
	# Read HTML file
	with open(file_path, 'r') as f:
		# Parse HTML using BeautifulSoup
		soup = BeautifulSoup(f, 'html.parser')
	# Find all tables in the HTML
	tables = soup.find_all('table')
	# Read tables into DataFrame using read_html()
	df = pd.read_html(str(tables))[0]
	return df

# File path
html_file_path = 'data/geeks_for_geeks.html'

# Read HTML file using BeautifulSoup with read_html()
df = read_html_with_beautiful_soup(html_file_path)

# Display DataFrame
print("Approach 2 Output:")
print(df)

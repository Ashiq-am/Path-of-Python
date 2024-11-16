import pandas as pd

def read_html_with_read_html(file_path):
	# Read HTML file into DataFrame using read_html()
	df = pd.read_html(file_path)[0]
	return df

# File path
html_file_path = 'data/geeks_for_geeks.html'

# Read HTML file using read_html() function
df = read_html_with_read_html(html_file_path)

# Display DataFrame
print("Approach 1 Output:")
print(df)

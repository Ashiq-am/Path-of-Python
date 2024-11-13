from bs4 import BeautifulSoup

# Open the HTML file in read mode
with open('a.html', 'r') as file:
	# Create a BeautifulSoup object
	soup = BeautifulSoup(file, 'html.parser')

	# Extract and print specific elements
	print(soup.title)
	print(soup.body)

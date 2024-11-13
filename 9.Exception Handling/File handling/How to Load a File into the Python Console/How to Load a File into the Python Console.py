import json
import csv
from bs4 import BeautifulSoup

# Open the text file in read mode
with open('a.txt', 'r') as file:
	# Read the entire content of the file
	text_content = file.read()

# Print the content to the console
print(text_content)

# Open the JSON file in read mode
with open('a.json', 'r') as file:
	# Load the JSON content into a Python dictionary
	json_content = json.load(file)

# Print the content to the console
print(json_content)

# Open the CSV file in read mode
with open('a.csv', 'r') as file:
	# Create a CSV reader object
	csv_reader = csv.reader(file)

	# Iterate through rows and print each row
	for row in csv_reader:
		print(row)

# Open the HTML file in read mode
with open('a.html', 'r') as file:
	# Create a BeautifulSoup object
	soup = BeautifulSoup(file, 'html.parser')

	# Extract and print specific elements
	print(soup.title)
	print(soup.body)

import csv

# Open the CSV file in read mode
with open('a.csv', 'r') as file:
	# Create a CSV reader object
	csv_reader = csv.reader(file)

	# Iterate through rows and print each row
	for row in csv_reader:
		print(row)

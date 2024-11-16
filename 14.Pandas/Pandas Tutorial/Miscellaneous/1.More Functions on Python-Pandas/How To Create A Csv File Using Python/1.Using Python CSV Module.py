# importing csv
import csv

# Data
data = [
	['Name', 'Age', 'City'],
	['Aman', 28, 'Pune'],
	['Poonam', 24, 'Jaipur'],
	['Bobby', 32, 'Delhi']
]

# File path for the CSV file
csv_file_path = 'example.csv'

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
	# Create a csv.writer object
	writer = csv.writer(file)
	# Write data to the CSV file
	writer.writerows(data)

# Print a confirmation message
print(f"CSV file '{csv_file_path}' created successfully.")

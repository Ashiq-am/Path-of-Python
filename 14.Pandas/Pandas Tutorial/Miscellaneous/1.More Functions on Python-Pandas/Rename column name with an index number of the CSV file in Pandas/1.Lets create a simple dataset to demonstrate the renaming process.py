# Import the csv module
import csv

# Define the data as a list of dictionaries
data = [
	{"Name": "Alice", "Age": 12, "Gender": "F", "Grade": "A"},
	{"Name": "Bob", "Age": 13, "Gender": "M", "Grade": "B"},
	{"Name": "Charlie", "Age": 14, "Gender": "M", "Grade": "C"},
	{"Name": "David", "Age": 12, "Gender": "M", "Grade": "A"},
	{"Name": "Eve", "Age": 13, "Gender": "F", "Grade": "B"}
]

# Open a new csv file for writing
with open("data.csv", "w") as file:
	# Create a csv writer object
	writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Gender", "Grade"])
	# Write the header row
	writer.writeheader()
	# Write the data rows
	writer.writerows(data)

# Close the file
file.close()

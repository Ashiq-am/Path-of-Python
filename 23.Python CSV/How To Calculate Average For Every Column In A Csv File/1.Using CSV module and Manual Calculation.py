# Python program for the above approach
import csv

# Open the CSV file for reading
with open('data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	headers = next(reader) # Read the header row

	# Initialize variables to store column sums and counts
	sums = [0] * len(headers)
	counts = [0] * len(headers)

	# Iterate through each row in the CSV file
	for row in reader:
		for i, value in enumerate(row):
			try:
				num = float(value)
				sums[i] += num
				counts[i] += 1
			except ValueError:
				pass # Ignore non-numeric values

	# Calculate and print the average for each column
	for i, header in enumerate(headers):
		average = sums[i] / counts[i] if counts[i] != 0 else 0
		print(f"Average {header}: {average:.2f}")

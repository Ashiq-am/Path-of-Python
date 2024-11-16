import csv

with open("StudentPerformance.csv", "r") as source, open("target.csv", "w") as target:
	reader = csv.reader(source)
	writer = csv.writer(target)

	for row in reader:
		if row[2].isdigit():
			new_row = [row[0], str(int(row[2]) + 10)]
		else:
			new_row = row # Handle rows with non-numerical data at index 2

		# Print the selected or manipulated row to the console
		print(new_row)

		# Write the row to the target CSV file
		writer.writerow(new_row)
	print('\ncsv Data copied to target csv files')

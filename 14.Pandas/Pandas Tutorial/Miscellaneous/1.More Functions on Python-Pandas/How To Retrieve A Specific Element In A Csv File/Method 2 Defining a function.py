import csv

def retrieve_csv_element(csv_file_path, row_index, column_index):
	try:
		# Read the CSV file
		with open(csv_file_path, 'r') as csv_file:
			# Create a CSV reader object
			csv_reader = csv.reader(csv_file)

			# Iterate through the rows
			for current_row_index, row in enumerate(csv_reader):
				# Check if the current row matches the desired row index
				if current_row_index == row_index:
					# Check if the current row has enough columns
					if column_index < len(row):
						# Retrieve the specific element and return it
						return row[column_index]
					else:
						raise ValueError(
							f"Column index {column_index} is out of range for row {row_index}")

			# If the desired row index is not found
			raise ValueError(
				f"Row index {row_index} not found in the CSV file")

	except Exception as e:
		print(f"An error occurred: {e}")

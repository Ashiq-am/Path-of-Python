# Example usage
csv_file_path = "StudentPerformance.csv"

row_index = 4
column_index = 0

element = retrieve_csv_element(csv_file_path, row_index, column_index)
if element is not None:
	print(f"Element at row {row_index}, column {column_index}: {element}")

import re

def open_file_by_regex_and_extract(file_pattern):
	# List all files with timestamps in their names
	files = ["20220101_report.txt", "20220215_data.csv", "20220320_summary.docx"]

	# Use regex groups to extract relevant information
	pattern = re.compile(r'(\d{4})(\d{2})(\d{2})_' + file_pattern)
	for file_name in files:
		match = pattern.match(file_name)
		if match:
			year, month, day = match.groups()
			print(f"Date: {year}-{month}-{day}, File: {file_name}")

# Example usage
open_file_by_regex_and_extract(r'.*\.txt')

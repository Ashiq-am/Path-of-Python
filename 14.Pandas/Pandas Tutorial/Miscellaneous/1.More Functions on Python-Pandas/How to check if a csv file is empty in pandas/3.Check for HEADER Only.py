with open("your_file.csv", "r") as file:
	line_count = sum(1 for line in file)

if line_count <= 1:
	print("The CSV file contains only the header.")
else:
	df = pd.read_csv("your_file.csv")
	# Process the data.

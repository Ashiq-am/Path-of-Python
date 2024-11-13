import csv

# exporting a string variable into the csv file
input_variable = "GeeksForGeeks"

# Example.csv gets created in the current working directory
with open('Example.csv', 'w', newline = '') as csvfile:
	my_writer = csv.writer(csvfile, delimiter = ' ')
	my_writer.writerow(input_variable)

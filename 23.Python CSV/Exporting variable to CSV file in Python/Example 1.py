import csv

# exporting a list variable into the csv file
input_variable = ['This', 'is', 'Geeks',
				'For', 'Geeks','list']

# Example.csv gets created in the current working directory
with open('Example.csv', 'w', newline = '') as csvfile:
	my_writer = csv.writer(csvfile, delimiter = ' ')
	my_writer.writerow(input_variable)

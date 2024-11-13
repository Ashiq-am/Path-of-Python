import csv

# 2D list of variables (tabular data with rows and columns)
input_variable = [
	['S.no','name','e-mail'],
	[1,'meesha','meesh@email.com'],
	(2,'abhilasha','ab@email.com'),
	(3,'arav','arav123@email.com')
]

# Example.csv gets created in the current working directory
with open ('Example.csv','w',newline = '') as csvfile:
	my_writer = csv.writer(csvfile, delimiter = ' ')
	my_writer.writerows(input_variable)

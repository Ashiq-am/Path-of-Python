# data to be stored in csv in form of list of list
data = [
	['Name', 'Gender', 'Age', 'Course'],
	['Aman', 'M', 22, 'B.Tech'],
	['Pankaj', 'M', 24, 'M.Tech'],
	['Beena', 'F', '23', 'MBA']
]

# file path of csv to be stored
csv_file_path = 'ex3.csv'

# opening file in write mode using a context manager
with open(csv_file_path, mode='w') as file:
	for row in data:
		file.write(','.join(map(str, row)) + '\n') # writing data row by row

print(f"CSV file '{csv_file_path}' created successfully!!!")

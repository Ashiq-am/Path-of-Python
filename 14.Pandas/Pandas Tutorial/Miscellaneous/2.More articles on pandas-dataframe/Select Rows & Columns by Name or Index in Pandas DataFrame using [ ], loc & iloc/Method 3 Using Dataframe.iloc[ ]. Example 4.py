# import pandas
import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
			('Saumya', 32, 'Delhi', 25000),
			('Aaditya', 25, 'Mumbai', 40000),
			('Saumya', 32, 'Delhi', 35000),
			('Saumya', 32, 'Delhi', 30000),
			('Saumya', 32, 'Mumbai', 20000),
			('Aaditya', 40, 'Dehradun', 24000),
			('Seema', 32, 'Delhi', 70000)
			]

# Create a DataFrame object from list
df = pd.DataFrame(employees,
				columns =['Name', 'Age',
			'City', 'Salary'])

# Using the operator .iloc[]
# to select all the rows with
# some particular columns
result = df.iloc[:, [0, 1]]

# Show the dataframe
result

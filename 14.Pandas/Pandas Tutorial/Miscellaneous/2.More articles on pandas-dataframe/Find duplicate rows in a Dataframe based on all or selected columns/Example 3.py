# import pandas library
import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi'),
			('Saumya', 32, 'Delhi'),
			('Aaditya', 25, 'Mumbai'),
			('Saumya', 32, 'Delhi'),
			('Saumya', 32, 'Delhi'),
			('Saumya', 32, 'Mumbai'),
			('Aaditya', 40, 'Dehradun'),
			('Seema', 32, 'Delhi')
			]

# Creating a DataFrame object
df = pd.DataFrame(employees,
				columns = ['Name', 'Age', 'City'])

# Selecting duplicate rows based
# on 'City' column
duplicate = df[df.duplicated('City')]

print("Duplicate Rows based on City :")

# Print the resultant Dataframe
duplicate

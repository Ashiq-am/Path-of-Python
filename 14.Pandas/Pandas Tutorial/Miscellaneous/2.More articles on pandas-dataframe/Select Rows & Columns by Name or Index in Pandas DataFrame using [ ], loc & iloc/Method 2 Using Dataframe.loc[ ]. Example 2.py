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

# Set index on a Dataframe
df.set_index("Name",
			inplace = True)

# Using the operator .loc[]
# to select multiple rows
result = df.loc[["Stuti", "Seema"]]

# Show the dataframe
result

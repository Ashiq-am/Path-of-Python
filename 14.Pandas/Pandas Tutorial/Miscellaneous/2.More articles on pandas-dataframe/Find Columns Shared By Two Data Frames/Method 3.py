# Importing libraries
import pandas as pd

# Creating Dataframes
a = [{'Name': 'abc', 'Age': 8, 'Grade': 3},
	{'Name': 'xyz', 'Age': 9, 'Grade': 3}]

df1 = pd.DataFrame(a)
b = [{'ID': 1,'Name': 'abc', 'Age': 8},
	{'ID': 2,'Name': 'xyz', 'Age': 9}]

df2 = pd.DataFrame(b)

# printing Dataframes
display(df1)
display(df2)

# Finding Common columns
a = df1.columns & df2.columns

# Printing common columns
print ("Common Columns:",a)

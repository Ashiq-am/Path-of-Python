# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Name': ['John', 'Emily', 'Smith', 'Joe'],
	'Gender': ['Male', 'Female', 'Male', 'Female'],
	'Salary(in $)': [20, 40, 35, 28]})

print("Dataset")
print(df)
print("-"*40)

# creating pivot table
table = pd.pivot_table(df, index=['Gender', 'Name'])

# calculating percentage
table['% Income'] = (table['Salary(in $)']/table['Salary(in $)'].sum())*100

# display table
print("Pivot Table")
print(table)

# importing pandas library
import pandas as pd

# creating and initializing a nested list
students = [['jackma', 34, 'Sydeny', 'Australia'],
			['Ritika', 30, 'Delhi', 'India'],
			['Vansh', 31, 'Delhi', 'India'],
			['Nany', 32, 'Tokyo', 'Japan'],
			['May', 16, 'New York', 'US'],
			['Michael', 17, 'las vegas', 'US']]

# Create a DataFrame object
df = pd.DataFrame(students,
				columns=['Name', 'Age', 'City', 'Country'],
				index=['a', 'b', 'c', 'd', 'e', 'f'])

# creating columns 'Age' and 'ID' at
# 2nd and 3rd position using
# dataframe.insert() function
df.insert(2, "Marks", [90, 70, 45, 33, 88, 77], True)
df.insert(3, "ID", [101, 201, 401, 303, 202, 111], True)


# Displaying the Data frame
df

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

# creating columns 'Admissionnum' and 'Percentage'
# using dataframe.assign() function
df = df.assign(Admissionnum=[250, 800, 1200, 300, 400, 700],
			Percentage=['85%', '90%', '75%', '35%', '60%', '80%'])

# Displaying the Data frame
df

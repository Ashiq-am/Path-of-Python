# Python program to implement
# axes attribute in a dataframe object
import pandas as pd
# Creating a 2D dictionary having values as
# dictionary object
dict = {"Sales": {'Name': 'Shyam',
				'Age': 23, 'Gender': 'Male'},
		"Marketing": {'Name': 'Neha', 'Age': 22,
					'Gender': 'Female'}}

# Creating a data frame object
data_frame = pd.DataFrame(dict)

# printing this data frame on output screen
display(data_frame)

# Implementing axes attribute for this data frame
print(data_frame.axes)

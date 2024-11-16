# Python program to implement
# empty attribute in a dataframe object
import pandas as pd

# Creating a 2D dictionary having values as
# dictionary object
dict = {"Sales": {'Name': 'Shyam',
				'Age': 23,
				'Gender': 'Male'},
		"Marketing": {'Name': 'Neha',
					'Age': 22,
					'Gender': 'Female'}}
# Creating a data frame object
data_frame = pd.DataFrame(dict)

# printing this data frame on output screen
display(data_frame)

# Implementing empty attribute for this data frame
print("Is this DataFrame empty?")
print(data_frame.empty)

# Now we will create another dataframe
print("..Another data frame..")

# Creating a 2D empty dictionary
dict2 = {}

# Creating a data frame object
data_frame = pd.DataFrame(dict2)

# printing this DataFrame on output screen
display(data_frame)

# Implementing empty attribute for this data frame
print("Is this DataFrame empty?")
print(data_frame.empty)

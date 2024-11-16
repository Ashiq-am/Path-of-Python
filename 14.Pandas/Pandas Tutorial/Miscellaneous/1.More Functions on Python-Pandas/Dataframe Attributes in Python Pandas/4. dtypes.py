# Python program to implement
# dtypes attribute in a dataframe object
import pandas as pd

# Creating a 2D dictionary having values as
# dictionary object
dict = {"Sales": {'Name': 'Shyam',
				'Age': 23, 'Gender': 'Male'},
		"Marketing": {'Name': 'Neha',
					'Age': 22, 'Gender': 'Female'}}

# Creating a data frame object
data_frame = pd.DataFrame(dict)

# printing this data frame on output screen
display(data_frame)

# Implementing dtypes attribute for this
# data frame
print(data_frame.dtypes)

# Now we will create another dataframe of same
# data type in a particular column
print("..Another data frame..")

# Creating a 2D dictionary
dict2 = {"Student": ["Arnav", "Neha",
					"Priya", "Rahul"],
		"Marks": [85, 92, 78, 83],
		"Sports": ["Cricket", "Volleyball",
					"Hockey", "Badminton"]}

# Creating another data frame object
data_frame = pd.DataFrame(dict2)

# printing this data frame on output screen
display(data_frame)

# Implementing dtypes attribute for this
# data frame
print(data_frame.dtypes)

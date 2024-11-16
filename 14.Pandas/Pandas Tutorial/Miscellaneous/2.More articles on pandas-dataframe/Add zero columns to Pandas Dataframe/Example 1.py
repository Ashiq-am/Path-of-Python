# import pandas library
import pandas as pd

# creating dictionary of lists
dict = {'name': ["sohom", "rakesh", "rajshekhar", "sumit"],
		'department': ["ECE", "CSE", "EE", "MCA"],
		'CGPA': [9.2, 8.7, 8.6, 7.7]}

# creating a dataframe
df = pd.DataFrame(dict)

print("data frame before adding the column:")
display(df)

# creating a new column
# of zeroes to the
# dataframe
df['new'] = 0

# showing the dataframe
print("data frame after adding the column:")
display(df)

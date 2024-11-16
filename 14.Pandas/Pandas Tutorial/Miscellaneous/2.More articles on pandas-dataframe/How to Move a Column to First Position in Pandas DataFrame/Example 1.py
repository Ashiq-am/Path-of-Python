import pandas as pd


# define data
from IPython.core.display import display

data = {'Age': [55, 20, 35, 10], 'Name': ['Rohan', 'Ritik', 'Sangeeta', 'Yogesh'],
		'Address': ['Lucknow', 'Delhi', 'Haridwar', 'Nainital'],
		'Phone Number': [123456789, 234567890, 3456789012, 4567890123]}

# create dataframe
df = pd.DataFrame(data)

# print original dataframe
print("Original Dataframe")
display(df)

# shift column 'Name' to first position
first_column = df.pop('Name')

# insert column using insert(position,column_name,
# first_column) function
df.insert(0, 'Name', first_column)

print()
print("After Shifting column to first position")
display(df)

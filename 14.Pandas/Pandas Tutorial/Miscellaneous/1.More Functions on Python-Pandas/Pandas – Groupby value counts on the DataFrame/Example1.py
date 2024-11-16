# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({
	'Course': ['BBA', 'BCA', 'BBA', 'BCA', 'BCA'],
	'Student Name': ['Rishabh', 'Rahul', 'Suraj', 'Mukul', 'Vinit'],
	'Age': [21, 22, 23, 22, 23]})


# print original dataframe
print("original dataframe")
display(df)

# counts Groupby value
df = df.groupby(['Course', 'Student Name', 'Age']).size().unstack(fill_value=0)

# print dataframe
print("Result :")
display(df)

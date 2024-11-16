# import pandas
import pandas as pd

# create dataframe
from Tools.scripts.dutree import display

df = pd.DataFrame({
	'Name': ['Mukul', 'Rohit', 'Suraj', 'Rohan', 'Rajan'],
	'Course': ['BBA', 'BCA', 'MBA', 'BCA', 'BBA'],
	'Roll No': [21, 22, 23, 24, 25]})

# print dataframe
print("\n *** Original DataFrames ** ")
display(df)


# create series
s6 = pd.Series(['Vedansh', 'MBA', 29], index=['Name', 'Course', 'Roll No'])

# print series
print("\n *** series ** ")
print(s6)

# create dictioneries
dicts = [{'Name': 'Aakash', 'Course': 'BCA', 'Roll No': 30}]

# print dictioneries
print("\n ** Dictionary ** ")
print(dicts)


# combined data
df = df.append(dicts, ignore_index=True, sort=False)
print("\n ** Combined Data **")
display(df)

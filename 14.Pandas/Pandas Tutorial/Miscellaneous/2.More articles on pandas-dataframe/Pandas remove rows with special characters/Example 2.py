# importing package
import pandas as pd

# load dataset
df = pd.read_csv("data2.csv")

# view dataset
print(df)

# select and then merge rows
# with special characters
print(df[df.ID.str.contains(r'[^0-9a-zA-Z]') |
		df.Name.str.contains(r'[^0-9a-zA-Z]') |
		df.Age.str.contains(r'[^0-9a-zA-Z]') |
		df.Country.str.contains(r'[^0-9a-zA-Z]')])

# drop the rows
print(df.drop(df[df.ID.str.contains(r'[^0-9a-zA-Z]') |
				df.Name.str.contains(r'[^0-9a-zA-Z]') |
				df.Age.str.contains(r'[^0-9a-zA-Z]') |
				df.Country.str.contains(r'[^0-9a-zA-Z]')].index))

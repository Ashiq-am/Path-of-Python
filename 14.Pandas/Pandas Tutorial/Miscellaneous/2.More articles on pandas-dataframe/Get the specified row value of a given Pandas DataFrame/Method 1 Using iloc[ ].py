# import pandas library
import pandas as pd

# Creating a dictionary
d = {'sample_col1': [1, 2, 3],
	'sample_col2': [4, 5, 6],
	'sample_col3': [7, 8, 9]}

# Creating a Dataframe
df = pd.DataFrame(d)

# show the dataframe
print(df)

print()

# Select Row No. 2
print(df.iloc[2])

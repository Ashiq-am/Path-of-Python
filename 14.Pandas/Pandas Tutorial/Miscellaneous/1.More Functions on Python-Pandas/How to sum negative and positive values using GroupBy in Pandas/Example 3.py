# Import Necessary Libraries
import pandas as pd
import numpy as np

# Creating a DataFrame with random values
df = pd.DataFrame({'Name': ['Aryan', 'Nityaa', 'Dhruv',
							'Dhruv', 'Nityaa', 'Aryan',
							'Nityaa', 'Aryan', 'Aryan',
							'Dhruv', 'Nityaa', 'Dhruv',
							'Dhruv'],
				'Marks': [90, 93, 78, 56, 34, 12, 67,
							45, 78, 92, 29, 88, 81]})
print(df)

# Group By dataframe on categorical values
d = df.groupby(df['Name'])

# creating lambda function to calculate
# positive as well as negative values
def pos(col):
    return col[col > 0].sum()

def neg(col):
    return col[col < 0].sum()


# Apply lambda function to particular
# column
print(d['Marks'].agg([('negative_values', neg),
					('positive_values', pos)
					]))

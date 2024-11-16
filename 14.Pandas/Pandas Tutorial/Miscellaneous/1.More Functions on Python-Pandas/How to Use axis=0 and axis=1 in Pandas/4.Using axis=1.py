# importing packages
import pandas as pd

# creating a dataset
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],
				[7, 8, 9], [10, 11, 12]],
				columns=['a', 'b', 'c'])

# viewing the dataFrame
print(df)

# finding mean by columns
df.mean(axis='columns')

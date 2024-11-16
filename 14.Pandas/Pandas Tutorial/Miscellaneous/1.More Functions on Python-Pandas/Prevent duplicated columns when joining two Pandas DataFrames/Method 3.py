# import python pandas package
import pandas as pd

# import the numpy package
import numpy as np

# Create sample dataframe data1 and data2
data1 = pd.DataFrame(np.random.randint(100, size=(1000, 3)),
					columns=['EMI', 'Salary', 'Debt'])
data2 = pd.DataFrame(np.random.randint(100, size=(1000, 3)),
					columns=['Salary', 'Debt', 'Bonus'])

# Find the columns that aren't in the first DataFrame
different_cols = data2.columns.difference(data1.columns)

# Filter out the columns that are different.
# You could pass in the df2[diff_cols]
# directly into the merge as well.
data3 = data2[diff_cols]

# Merge the DataFrames
df_merged = pd.merge(data1, data3, left_index=True,
					right_index=True, how='inner')

import pandas as pd

# Creating a data frame along with column name
df = pd.DataFrame([[2, 2.5, 100, 4.5, 8.8, 95]], columns=[
				'int', 'float', 'int', 'float', 'float', 'int'])

# Iter over the data frame rows
# # using df.iterrows()
itr = next(df.iterrows())[1]
itr

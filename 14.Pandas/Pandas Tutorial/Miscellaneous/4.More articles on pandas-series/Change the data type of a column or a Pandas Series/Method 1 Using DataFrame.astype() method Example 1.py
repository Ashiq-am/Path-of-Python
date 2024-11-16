# importing the pandas library
import pandas as pd

# creating a DataFrame
df = pd.DataFrame({'srNo': [1, 2, 3],
				'Name': ['Geeks', 'for',
							'Geeks'],
				'id': [111, 222,
						333]})
# show the dataframe
print(df)

# show the datatypes
print(df.dtypes)

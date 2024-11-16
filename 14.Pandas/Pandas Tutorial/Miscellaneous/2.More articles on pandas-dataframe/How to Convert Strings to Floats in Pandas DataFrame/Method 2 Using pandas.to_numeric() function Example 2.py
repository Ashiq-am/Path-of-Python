# importing pandas as pd
import pandas as pd

# dictionary
Data = {'Year': ['2016', '2017',
				'2018', '2019'],
		'Inflation Rate': ['4.47', '5',
						'No data', '4.1']}

# create a dataframe
df = pd.DataFrame(Data)

# converting each value of column to a string
df['Inflation Rate'] = pd.to_numeric(df['Inflation Rate'],
									errors = 'coerce')

# show the dataframe
print(df)

# show the data types
print (df.dtypes)

# importing pandas library
import pandas as pd

# creating a dictionary
Data = {'Year': ['2016', '2017',
				'2018', '2019'],
		'Inflation Rate': ['4.47', '5',
							'5.98', '4.1']}
# create a dataframe
df = pd.DataFrame(Data)

# converting each value of column to a string
df['Inflation Rate'] = pd.to_numeric(df['Inflation Rate'])

# show the dataframe
print(df)

# show the data types
print (df.dtypes)

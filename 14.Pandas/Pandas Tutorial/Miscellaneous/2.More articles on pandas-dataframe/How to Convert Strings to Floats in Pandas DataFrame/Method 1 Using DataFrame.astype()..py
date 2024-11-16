# importing pandas library
import pandas as pd

# dictionary
Data = {'Year': ['2016', '2017',
				'2018', '2019'],
		'Inflation Rate': ['4.47', '5',
						'5.98', '4.1']}
# create a dataframe
df = pd.DataFrame(Data)

# converting each value
# of column to a string
df['Inflation Rate'] = df['Inflation Rate'].astype(float)

# show the dataframe
print(df)

# show the datatypes
print (df.dtypes)

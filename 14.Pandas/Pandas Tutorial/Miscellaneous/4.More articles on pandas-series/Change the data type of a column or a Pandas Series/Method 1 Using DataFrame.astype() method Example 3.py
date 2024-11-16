# import pandas library
import pandas as pd

# dictionary
result_data = {'name': ['Alia', 'Rima', 'Kate',
						'John', 'Emma', 'Misa',
						'Matt'],
		'grade': [13.5, 7.1, 11.5,
				3.77, 8.21, 21.22,
				17.5],
		'qualify': ['yes', 'no', 'yes',
					'no', 'no', 'yes',
					'yes']}

# create a dataframe
df = pd.DataFrame(result_data)

# show the dataframe
print(df)

#show the datatypes
print(df.dtypes)

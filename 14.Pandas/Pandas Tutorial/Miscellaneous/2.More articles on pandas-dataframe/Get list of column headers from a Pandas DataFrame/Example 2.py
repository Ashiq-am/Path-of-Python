# importing pandas as pd
import pandas as pd

# creating the dataframe
my_df = {'Students': ['A', 'B', 'C', 'D'],
		'BMI': [22.7, 18.0, 21.4, 24.1],
		'Religion': ['Hindu', 'Islam',
					'Christian', 'Sikh']}
df = pd.DataFrame(my_df)
display("The DataFrame :")
display(df)

# print the list of all the column headers
display("The column headers :")
display(list(df.columns.values))

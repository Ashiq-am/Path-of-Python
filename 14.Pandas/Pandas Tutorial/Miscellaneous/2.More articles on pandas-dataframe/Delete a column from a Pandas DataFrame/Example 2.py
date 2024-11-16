# importing the module
import pandas as pd

# creating a DataFrame
my_df = {'Students': ['A', 'B', 'C', 'D'],
		'BMI': [22.7, 18.0, 21.4, 24.1],
		'Religion': ['Hindu', 'Islam',
					'Christian', 'Sikh']}
df = pd.DataFrame(my_df)
display("Original DataFrame")
display(df)

# deleting a column
del df['Religion']

display("DataFrame after deletion")
display(df)

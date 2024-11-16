# Import the library
import pandas as pd

# dataframe
df = pd.DataFrame({'Name': ['John', 'Jack', 'Shri',
							'Krishna', 'Smith', 'Tessa'],
				'Maths': [5, 3, 9, 10, 6, 3]})

# Adding the result column
df['Result'] = df['Maths'].apply(lambda x: 'Pass' if x>=5 else 'Fail')

print(df)

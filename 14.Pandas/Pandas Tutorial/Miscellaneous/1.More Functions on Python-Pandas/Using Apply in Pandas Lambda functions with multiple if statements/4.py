# Import the library
import pandas as pd

# dataframe
df = pd.DataFrame({'Name': ['John', 'Jack', 'Shri',
							'Krishna', 'Smith', 'Tessa'],
				'Maths': [5, 3, 9, 10, 6, 3]})

# Defining all the conditions inside a function
def condition(x):
	if x>8:
		return "No need"
	elif x>=5 and x<=7:
		return "Hold decision"
	else:
		return 'Need'

# Applying the conditions
df['Maths_Spl Class'] = df['Maths'].apply(condition)

print(df)

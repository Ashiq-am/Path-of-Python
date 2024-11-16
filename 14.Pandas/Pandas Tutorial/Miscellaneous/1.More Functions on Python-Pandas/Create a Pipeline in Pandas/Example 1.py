# importing pandas library
import pandas as pd

# Create empty dataframe
df = pd.DataFrame()

# Creating a simple dataframe
df['name'] = ['Reema', 'Shyam', 'Jai',
			'Nimisha', 'Rohit', 'Riya']
df['gender'] = ['Female', 'Male', 'Male',
				'Female', 'Male', 'Female']
df['age'] = [31, 32, 19, 23, 28, 33]

# View dataframe
df

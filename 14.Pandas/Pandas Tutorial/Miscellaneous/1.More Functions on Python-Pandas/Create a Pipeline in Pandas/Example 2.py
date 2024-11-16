# importing the package
import pdpipe as pdp
import pandas as pd

# creating a emplty dataframe named dataset
dataset = pd.DataFrame()

# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai',
				'Nimisha', 'Rohit', 'Riya']

dataset['gender'] = ['Female', 'Male', 'Male',
					'Female', 'Male', 'Female']

dataset['age'] = [31, 32, 19, 23, 28, 33]

dataset['department'] = ['Accounts', 'Management',
						'IT', 'IT', 'Managemnt',
						'Advertising']

dataset['index'] = [1, 2, 3, 4, 5, 6]

# View dataframe
dataset

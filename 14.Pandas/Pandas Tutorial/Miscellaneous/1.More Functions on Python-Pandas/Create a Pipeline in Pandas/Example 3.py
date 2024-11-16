# importing the package
import pdpipe as pdp
import pandas as pd

# function to assign
# senior and junior in post
def fun(x):
	if x > 30:
		return "Senior"
	else:
		return "Junior"


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

# creating new column
# comparing with another column
# and applying the function
dataset['post'] = dataset['age'].apply(fun)

# display dataframe
dataset

# Import required libraries
import pandas as pd
import numpy as np

# Dictionary
data = {
	'Name': ['Geek1', 'Geek2',
			'Geek3', 'Geek4'],
'Salary': [18000, 20000,
			15000, 35000]}

# Create a dataframe
data = pd.DataFrame(data,
					columns = ['Name',
							'Salary'])

# Show the dataframe
data

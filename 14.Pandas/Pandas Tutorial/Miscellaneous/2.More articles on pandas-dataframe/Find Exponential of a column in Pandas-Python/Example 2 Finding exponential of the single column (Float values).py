# importing pandas and
# numpy libraries
import pandas as pd
import numpy as np

# creating and initializing a list
values= [ ['Rohan', 5, 50.59], ['Elvish', 2, 90.57],
		['Deepak', 10, 98.51], ['Soni', 4, 40.24],
		['Radhika', 1, 99.05], ['Vansh', 15, 85.56] ]

# creating a pandas dataframe
df = pd.DataFrame(values, columns = ['Name',
									'University_Rank',
									'University_Marks'])

# finding the exponential value
# of cloumn using np.exp() function
df['exp_value'] = np.exp(df['University_Marks'])

# displaying the data frame
df

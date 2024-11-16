# Python program to illustrate
# Add a new column in Pandas
# Data Frame Using a Dictionary

import pandas as pd

data_frame = pd.DataFrame([[i] for i in range(7)], columns =['data'])

# Introducing weeks as dictionary
weeks = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday',
4:'Thursday', 5:'Friday', 6:'Saturday'}

# Mapping the dictionary keys to the data frame.
data_frame['new_data_1'] = data_frame['data'].map(weeks)
print (data_frame)

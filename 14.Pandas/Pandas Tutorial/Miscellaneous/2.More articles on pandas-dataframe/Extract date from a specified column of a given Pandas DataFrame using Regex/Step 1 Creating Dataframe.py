# importing pandas and re library
import pandas as pd
import re as re

# creating data frame with column
# name,date_of_birth and age
df = pd.DataFrame({'Name': ['Akash', 'Shyam', 'Ayush',
							'Diksha', 'Radhika'],

				'date_of_birth': ['12/21/1998', '15/12/1998',
									'06/11/2000', '05/10/1998',
									'13/12/2010'],

				'Age': [21, 12, 20, 21, 10]})

# printing the original data frame
print("Printing the original dataframe")
df

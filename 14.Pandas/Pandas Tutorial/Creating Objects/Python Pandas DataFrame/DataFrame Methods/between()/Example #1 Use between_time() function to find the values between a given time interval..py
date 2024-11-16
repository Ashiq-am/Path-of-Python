# importing pandas as pd
import pandas as pd

# Creating row index values for dataframe
# Taken time frequency to be of 30 minutes interval
# Generating eight index value using "period = 8" parameter
ind = pd.date_range('01/01/2000', periods = 8, freq ='30T')

# Creating a dataframe with 2 columns
# using "ind" as the index for dataframe

df = pd.DataFrame({"A":[1, 2, 3, 4, 5, 6, 7, 8],
				"B":[10, 20, 30, 40, 50, 60, 70, 80]},
											index = ind)

# Printing the dataframe
df

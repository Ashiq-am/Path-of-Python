# importing pandas as pd
import pandas as pd

# Creating row index values for dataframe
# Taken time frequency to be of 12 hours interval

# Generating five index value using "period = 5" parameter
ind = pd.date_range('01/ 01/2000', periods = 5, freq ='12H')

# Creating a dataframe with 2 columns
# using "ind" as the index for our dataframe

df = pd.DataFrame({"A":[1, 2, 3, 4, 5],
				"B":[10, 20, 30, 40, 50]},
								index = ind)

# Printing the dataframe
# for visualization
df

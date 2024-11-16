# importing pandas as pd
import pandas as pd

# Creating a dataframe with "na" values.

df = pd.DataFrame({"A":[None, 1, 2, 3, None, None],
				"B":[11, 5, None, None, None, 8],
				"C":[None, 5, 10, 11, None, 8]})

# Printing the dataframe
df

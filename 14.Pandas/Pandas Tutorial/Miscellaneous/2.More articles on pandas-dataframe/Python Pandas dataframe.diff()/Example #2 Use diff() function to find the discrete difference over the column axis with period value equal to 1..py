# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[5, 3, 6, 4],
				"B":[11, 2, 4, 3],
				"C":[4, 3, 8, 5],
				"D":[5, 4, 2, 8]})

# To find the discrete difference
df.diff(axis = 1, periods = 1)

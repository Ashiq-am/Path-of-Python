# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[5, 3, None, 4],
				"B":[None, 2, 4, 3],
				"C":[4, 3, 8, 5],
				"D":[5, 4, 2, None]})

# To find the cumulative min
df.cummin(axis = 0, skipna = True)

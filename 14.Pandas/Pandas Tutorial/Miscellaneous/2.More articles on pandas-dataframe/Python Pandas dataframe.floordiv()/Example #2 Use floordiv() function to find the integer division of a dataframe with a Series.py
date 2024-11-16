# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[5, 3, 6, 4],
				"B":[11, 2, 4, 3],
				"C":[4, 3, 8, 5],
				"D":[5, 4, 2, 8]})

# creating series
sr = pd.Series([2, 1, 3, 1])

# applying floordiv() function
df.floordiv(sr, axis = 0)

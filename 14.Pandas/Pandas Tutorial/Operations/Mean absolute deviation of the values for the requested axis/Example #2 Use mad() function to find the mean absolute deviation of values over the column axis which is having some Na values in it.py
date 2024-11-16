# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[12, 4, 5, None, 1],
				"B":[7, 2, 54, 3, None],
				"C":[20, 16, 11, 3, 8],
				"D":[14, 3, None, 2, 6]})

# To find the mean absolute deviation
# skip the Na values when finding the mad value
df.mad(axis = 1, skipna = True)

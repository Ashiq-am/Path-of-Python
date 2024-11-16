# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[4, 5, 2, None],
				"B":[11, 2, None, 8],
				"C":[1, 8, 66, 4]})

# Skipna = True will skip all the Na values
# find maximum along column axis
df.idxmax(axis = 1, skipna = True)

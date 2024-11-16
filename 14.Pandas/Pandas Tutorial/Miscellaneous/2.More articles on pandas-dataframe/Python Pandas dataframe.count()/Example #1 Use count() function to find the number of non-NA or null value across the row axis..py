# importing pandas as pd
import pandas as pd

# Creating a dataframe using dictionary
df = pd.DataFrame({"A":[-5, 8, 12, None, 5, 3],
				"B":[-1, None, 6, 4, None, 3],
				"C":["sam", "haris", "alex", np.nan, "peter", "nathan"]})

# Printing the dataframe
df

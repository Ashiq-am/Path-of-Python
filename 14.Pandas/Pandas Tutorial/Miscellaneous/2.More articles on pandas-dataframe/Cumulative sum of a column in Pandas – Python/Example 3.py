import pandas as pd
import numpy as np

# Create a dataframe
df1 = pd.DataFrame({"A":[2, 3, 8, 14],
				"B":[1, 2, 4, 3],
				"C":[5, 3, 9,2]})

# Computing sum over Index axis
print(df1.cumsum(axis = 1))

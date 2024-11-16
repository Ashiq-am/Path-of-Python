import pandas as pd
import numpy as np

# Create a dataframe
df1 = pd.DataFrame({"A":[None, 3, 8, 14],
				"B":[1, None, 4, 3],
				"C":[5, 3, 9,None]})

# Computing sum over Index axis
print(df1.cumsum(axis = 0, skipna = True))

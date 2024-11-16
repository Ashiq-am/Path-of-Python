# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df = pd.DataFrame({"A":[1, 5, 3, 4, 2],
				"B":[3, None, 4, 3, 4],
				"C":[2, 2, 7, None, 4],
				"D":[None, 3, 6, 12, 7]})

# using prod() function to raise each element
# in df1 to the power of corresponding element in df2
df.prod(axis = 1, skipna = True)

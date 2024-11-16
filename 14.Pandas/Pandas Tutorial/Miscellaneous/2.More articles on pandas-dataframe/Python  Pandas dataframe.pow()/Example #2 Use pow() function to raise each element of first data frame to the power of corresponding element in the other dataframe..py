# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A":[14, 4, 5, 4, 1],
					"B":[5, 2, 54, 3, 2],
					"C":[20, 20, 7, 3, 8],
					"D":[14, 3, 6, 2, 6]})

# Creating the second dataframe
df2 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
					"B":[3, 2, 4, 3, 4],
					"C":[2, 2, 7, 3, 4],
					"D":[4, 3, 6, 12, 7]})

# using pow() function to raise each element
# in df1 to the power of corresponding element in df2
df1.pow(df2)

# importing pandas
import pandas as pd

# Using DataFrame() method from pandas module
df1 = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7],
					"b": [2, 3, 4, 2, 3, 4, 5],
					"c": [3, 4, 5, 2, 3, 4, 5],
					"d": [4, 5, 6, 2, 3, 4, 5],
					"e": [5, 6, 7, 2, 3, 4, 5]})

df2 = df1.loc[:, "c":"e":1]
print(df2)

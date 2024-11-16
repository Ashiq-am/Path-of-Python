# importing pandas
import pandas as pd
# Using DataFrame() method from pandas module
df1 = pd.DataFrame({"a": [1, 2, 3, 4, 5],
					"b": [2, 3, 4, 5, 6],
					"c": [3, 4, 5, 6, 7],
					"d": [4, 5, 7, 8, 9]})

df2 = df1.iloc[:, 1:3:1]
print(df2)

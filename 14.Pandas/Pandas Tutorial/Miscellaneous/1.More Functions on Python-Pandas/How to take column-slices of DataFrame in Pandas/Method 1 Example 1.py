# importing pandas
import pandas as pd

# Using DataFrame() method from pandas module
df1 = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4],
					"c": [3, 4, 5], "d": [4, 5, 6],
					"e": [5, 6, 7]})

df2 = df1.loc[:, "b":"d":2]
print(df2)

# importing the module
import pandas as pd

# creating the first DataFrame
df1 = pd.DataFrame({"fruit" : ["apple", "banana",
							"avocado", "grape"],
					"market_price" : [21, 14, 35, 38]})
display("The first DataFrame")
display(df1)

# creating the second DataFrame
df2 = pd.DataFrame({"fruit" : ["apple", "banana", "grape"],
					"wholesaler_price" : [65, 68, 71]})
display("The second DataFrame")
display(df2)

# joining the DataFrames
# here both common DataFrame elements are in df1 and df2,
# so it extracts apple, banana, grapes from df1 and df2.
display("The merged DataFrame")
pd.merge(df1, df2, on = "fruit", how = "inner")

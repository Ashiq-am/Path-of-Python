# importing the module
import pandas as pd

# creating the first DataFrame
df1 = pd.DataFrame({"fruit" : ["apple", "banana", "avocado"],
					"market_price" : [21, 14, 35]})
display("The first DataFrame")
display(df1)

# creating the second DataFrame
df2 = pd.DataFrame({"fruit" : ["banana", "apple", "avocado"],
					"wholesaler_price" : [65, 68, 75]})
display("The second DataFrame")
display(df2)

# joining the DataFrames
display("The merged DataFrame")
pd.merge(df1, df2, on = "fruit", how = "inner")

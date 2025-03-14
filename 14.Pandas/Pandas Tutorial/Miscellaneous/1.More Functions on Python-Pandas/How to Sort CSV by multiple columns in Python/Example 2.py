# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("diamonds.csv")

# sorting data frame by multiple columns
data.sort_values(["depth", "table"], axis=0,
				ascending=True, inplace=True)

# display
data.head(10)

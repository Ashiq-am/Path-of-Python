# import pandas library
import pandas as pd

# create a series
a = pd.Series(["ABC", "DEF",
			"GHI"])

# create a series
b = pd.Series(["JKL", "MNO",
			"PQR"])

# combine two series then
# create a dataframe
df = pd.DataFrame(a.append(b,
				ignore_index = True))
# show the dataframe
df

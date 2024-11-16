# import required module
import pandas as pd

# assign list
l = [[100, 200, 300], [10, None, 40],
	[20, 10, 30], [100, 200, 200]]

# create dataframe
df = pd.DataFrame(l, columns=["a", "b", "c"])

# use groupby() to generate sum
df.groupby(by=["b"]).sum()

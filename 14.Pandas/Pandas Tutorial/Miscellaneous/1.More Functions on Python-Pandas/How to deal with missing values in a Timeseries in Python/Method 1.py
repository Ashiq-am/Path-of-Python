# import the libraries
import pandas as pd
import numpy as np

# dataframe with index as timeseries
time_sdata = pd.date_range("09/10/2021", periods=9, freq="W")

df = pd.DataFrame(index=time_sdata)
print(df)

# there are four missing values
df["example"] = [10001.0, 10002.0, 10003.0, np.nan,
				10004.0, np.nan, np.nan, 10005.0, np.nan]

gfg1 = df.ffill()
print("Using ffill() function:-")
print(gfg1)

# here we are doing Backfill Missing Values
# in the output the last value has NaN because
# there is no backward value for that
gfg2 = df.bfill()
print("Using bfill() function:-")
print(gfg2)

# import modules
import pandas as pd

# read the data from the csv
data = pd.read_csv("daily-minimum-temperatures-in-blr.csv",
				header=0, index_col=0, parse_dates=True,
				squeeze=True)

# display top 15 data
data.head(15)

# lagplot
pd.plotting.lag_plot(data, lag=1)

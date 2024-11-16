# importing the module
import pandas as pd

# target year
year = "2020"

# day to be fetched
day = "MON"

# instantiating the parameters
start = year + "-01-01"
periods = 52
freq = "W-" + day

# fetching the days
days = pd.date_range(start = start,
					periods = periods,
					freq = freq)

# printing the days
print(days)

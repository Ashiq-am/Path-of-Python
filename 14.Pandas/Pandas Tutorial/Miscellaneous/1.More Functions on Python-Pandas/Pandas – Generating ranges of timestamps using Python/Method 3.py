# importing packages
import pandas as pd
import datetime

# range of dates
date_range = pd.period_range(
	start=datetime.datetime.today(), periods=10, freq='M')

# timestamp range
timestamp_range = [x.to_timestamp() for x in date_range]

# iterating through timestamp range
for i in timestamp_range:
	print(i)
print(type(i))

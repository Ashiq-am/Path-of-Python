# importing packages
import datetime
import pandas as pd

n_days = 10

# today's date in timestamp
base = pd.Timestamp.today()

# calculating timestamps for the next 10 days
timestamp_list = [base + datetime.timedelta(days=x) for x in range(n_days)]

# iterating through timestamp_list
for x in timestamp_list:
	print(x)

# importing packages
import pandas as pd
from datetime import datetime


# creating a range of timestamps
timestamp_list = pd.date_range(datetime.today(), periods=10).tolist()
for i in timestamp_list:
	print(i)
print(type(i))

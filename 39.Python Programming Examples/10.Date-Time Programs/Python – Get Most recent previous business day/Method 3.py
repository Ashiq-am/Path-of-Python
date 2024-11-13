# Python3 code to demonstrate working of
# Last business day
# using pd.tseries.offsets.BusinessDay(n)
import pandas as pd
from datetime import datetime

# initializing dates
test_date = datetime(2020, 2, 3)

# printing original date
print("The original date is : " + str(test_date))

# Creating Timestamp
ts = pd.Timestamp(str(test_date))

# Create an offset of 1 Business days
offset = pd.tseries.offsets.BusinessDay(n=1)

# getting result by subtracting offset
res = test_date - offset

# printing result
print("Last business day : " + str(res))

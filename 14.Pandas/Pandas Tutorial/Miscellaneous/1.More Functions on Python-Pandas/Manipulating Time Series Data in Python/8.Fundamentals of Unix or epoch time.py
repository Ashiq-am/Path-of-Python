# importing pandas
import pandas as pd
from datetime import datetime

# epoch time
epoch = 1598776989

# converting to timestamp
timestamp = pd.to_datetime(epoch, unit='s')
print(timestamp)

# converting it to a particular time zone
print(timestamp.tz_localize('UTC').tz_convert('Europe/Berlin'))

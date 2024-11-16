import pandas as pd

# Convert a string to a datetime object
date_string = '2023-07-17'
dateTime = pd.to_datetime(date_string)
print(dateTime)

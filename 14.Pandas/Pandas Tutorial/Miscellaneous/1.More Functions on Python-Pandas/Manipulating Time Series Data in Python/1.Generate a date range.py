# importing pandas
import pandas as pd

# creating a date range
Date_range = pd.date_range(start='1/12/2020', end='20/5/2021', freq='M')
print(Date_range)

print(type(Date_range))
print(type(Date_range[0]))

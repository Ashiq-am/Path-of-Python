import pandas as pd
import numpy as np

# Generate a DatetimeIndex with hourly frequency starting from '2023-02-01'
dates = pd.date_range('2023-02-01', periods=5, freq='H')
df = pd.DataFrame()
df['Datetime'] = dates
print(df)

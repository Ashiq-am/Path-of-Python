# importing the module
import pandas as pd

# generating 5 timestamp starting from '2020-01-01 00:00:00'
date1 = pd.Series(pd.date_range('2020-01-01 00:00:00',
								periods = 5, freq = 's'))

# coverting pandas series into data frame
df = pd.DataFrame(dict(GENERATEDTIMESTAMP = date1))

# extracting seconds from time stamp
df['extracted_seconds_timestamp'] = df['GENERATEDTIMESTAMP'].dt.second

# displaying DataFrame
display(df)

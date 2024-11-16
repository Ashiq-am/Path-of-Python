# importing the module
import pandas as pd

# generating 10 timestamp starting from '2016-10-10 09:21:12'
date1 = pd.Series(pd.date_range('2016-10-10 09:21:12',
								periods = 10, freq = 's'))

# coverting pandas series into data frame
df = pd.DataFrame(dict(GENERATEDTIMESTAMP = date1))

# extracting seconds from time stamp
df['extracted_seconds_timestamp'] = df['GENERATEDTIMESTAMP'].dt.second

# displaying DataFrame
display(df)

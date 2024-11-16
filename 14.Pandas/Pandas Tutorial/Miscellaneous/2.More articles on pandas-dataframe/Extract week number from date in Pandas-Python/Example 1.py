# importing pandas as pd
import pandas as pd

# creating a dictionary containing a date
dict = {'Date':["2015-06-17"]}

# converting the dictionary to a dataframe
df = pd.DataFrame.from_dict(dict)

# converting the date to the required format
df['Date'] = pd.to_datetime(df['Date'], errors ='coerce')
df.astype('int64').dtypes

# extracting the week from the date
weekNumber = df['Date'].dt.week

print(weekNumber)

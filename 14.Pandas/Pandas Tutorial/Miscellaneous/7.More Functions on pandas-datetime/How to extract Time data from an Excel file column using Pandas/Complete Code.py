# importing required module
import pandas as pd
import re

data = pd.read_excel("time_sample_data.xlsx");
print("Original DataFrame")
print(data)

# Create column for Date
data['New time'] = None
print(data)

# set index
index_set = data.columns.get_loc('Description')
index_time = data.columns.get_loc('New time')
print(index_set, index_time)

# define the time pattern in HH:MM:SS
time_pattern = r'([0-24]{2}\:[0-60]{2}\:[0-60]{2})'

# searching dataframe with time pattern
for row in range(0, len(data)):
    time = re.search(time_pattern, data.iat[row, index_set]).group()
    data.iat[row, index_time] = time

print("\n Final DataFrame")
data

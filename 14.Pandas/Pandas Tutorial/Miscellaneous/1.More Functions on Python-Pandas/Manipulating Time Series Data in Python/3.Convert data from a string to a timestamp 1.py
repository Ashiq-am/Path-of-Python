# importing pandas
import pandas as pd
from datetime import datetime

# string data
string_data = ['May-20-2021', 'May-21-2021', 'May-22-2021']
timestamp_data = [datetime.strptime(x, '%B-%d-%Y') for x in string_data]
print(timestamp_data)

Data = pd.DataFrame(timestamp_data, columns=['Date'])
print(Data.info())

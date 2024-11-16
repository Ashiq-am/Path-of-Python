# importing pandas
import pandas as pd

# creating string data
string_data = ['2020-01-31', '2020-02-29', '2020-03-31', '2020-04-30',
			'2020-05-31', '2020-06-30', '2020-07-31', '2020-08-31',
			'2020-09-30', '2020-10-31', '2020-11-30', '2020-12-31',
			'2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30']

Data = pd.DataFrame(string_data, columns=['Date'])
Data['Date'] = pd.to_datetime(Data['Date'])
print(Data.info())

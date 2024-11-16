# importing packages
import pandas as pd

# creating dataframe df(left)
df = pd.DataFrame()

df['time'] = pd.date_range('08/12/2021',
						periods=6, freq='4S')


df['data_name'] = ["Geeks", "Geeks", "Geeks",
				"Geeks", "GeeksforGeeks",
				"GeeksforGeeks"]
df['values'] = [1, 2, 3, 4, 5, 6]


# creating datafrframe df1(right)
df1 = pd.DataFrame()

df1['time'] = pd.date_range('08/12/2021',
							periods=6,
							freq='6S')


df1['data_name'] = ["Geeks", "Geeks", "Geeks",
					"Geeks", "GeeksforGeeks",
					"GeeksforGeeks"]
df1['values'] = [7, 8, 9, 10, 11, 12]

# using merge_asof for merging left and right
df2 = pd.merge_asof(df, df1, on='time', by='data_name',
					tolerance=pd.Timedelta('2s'))

# view data
print(df)
print(df1)
print(df2)

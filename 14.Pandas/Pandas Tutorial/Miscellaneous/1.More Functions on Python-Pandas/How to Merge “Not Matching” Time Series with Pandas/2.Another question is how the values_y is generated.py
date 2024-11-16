# importing packages
import pandas as pd

# creating dataframe
df = pd.DataFrame()

df['time'] = pd.date_range('08/12/2021',
						periods=6,
						freq='4S')


df['data_name'] = ["Geeks", "Geeks", "Geeks",
				"Geeks", "GeeksforGeeks",
				"GeeksforGeeks"]
df['values'] = [1, 2, 3, 4, 5, 6]
# creating dataframe
df1 = pd.DataFrame()

df1['time'] = pd.date_range('08/12/2021',
							periods=6, freq='6S')


df1['data_name'] = ["Geeks", "Geeks", "Geeks",
					"Geeks", "GeeksforGeeks",
					"GeeksforGeeks"]
df1['values'] = [7, 8, 9, 10, 11, 12]

# allow_exact_matches=True for merging
df3 = pd.merge_asof(df, df1, on='time',
					by='data_name',
					allow_exact_matches=True)
# view data
print(df3)
# allow_exact_matches=False for merging df and df1
df4 = pd.merge_asof(df, df1, on='time',
					by='data_name',
					allow_exact_matches=False)
# view data
print(df4)

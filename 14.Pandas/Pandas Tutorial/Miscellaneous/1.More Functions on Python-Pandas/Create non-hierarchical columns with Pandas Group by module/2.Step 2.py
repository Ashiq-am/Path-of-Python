# remove unwanted columns
remove_columns =['Website','Hqaddr','Hqzip', 'Hqtel',
				'Ceo','Ceo-title', 'Address', 'Ticker',
				'Prftchange', 'Assets', 'Totshequity']

df = df.drop(columns= remove_columns,axis = 1)
print(df.columns)

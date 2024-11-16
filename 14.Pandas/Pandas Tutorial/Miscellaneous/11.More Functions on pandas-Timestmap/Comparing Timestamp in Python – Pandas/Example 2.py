# Timestamps satisfying given condition
for i in range(len(df['year'])):
	if df['new_time'][i] < pd.Timestamp(2018, 1, 5, 12):
		print(df['new_time'][i])

df2 = pd.DataFrame()
for i in df.keys():
	df2 = pd.concat([df2, df[i]],
					axis = 0)

display(df2)

column_names = ["Company", "Price", "Change", "Volume"]
df = pd.DataFrame(columns=column_names)
for i in all:
	index = 0
	df.loc[index] = i
	df.index = df.index + 1
df = df.reset_index(drop=True)
df

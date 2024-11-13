Chat1 = df["Content"].str.split(":", n = 1,
								expand = True)
df['User'] = Chat1[0]
df['Message'] = Chat1[1]

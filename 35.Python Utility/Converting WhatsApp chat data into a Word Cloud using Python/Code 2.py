Chat = df["Convo"].str.split("-", n = 1,
							expand = True)
df['Time'] = Chat[0]
df['Content'] = Chat[1]

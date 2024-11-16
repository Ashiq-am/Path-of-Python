# To change the row indexes
df = pd.DataFrame({"A":['Tom','Nick','John','Peter'],
				"B":[25,16,27,18]})

# this will increase the row index value by 10 for each row
df = df.rename(index = lambda x: x + 10)

df

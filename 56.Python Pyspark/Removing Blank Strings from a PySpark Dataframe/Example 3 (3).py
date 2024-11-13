# filter out rows with blank strings in all the columns
df = df.filter(reduce(lambda x, y: x & y,
					[col(c) != '' for c in df.columns]))

# examine the dataframe
df.show()

# examine the dataframe
df.show()

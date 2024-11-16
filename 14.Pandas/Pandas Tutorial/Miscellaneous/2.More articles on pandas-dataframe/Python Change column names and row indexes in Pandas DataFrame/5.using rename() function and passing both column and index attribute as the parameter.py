df = df.rename(index = lambda x: x + 5,
			columns = lambda x: x +'x')

# increase all the row index label by value 5
# append a value 'x' at the end of each column name.
df

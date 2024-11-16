new = df.groupby(['States','Products'])['Sale'].agg('count').reset_index()
display(new)

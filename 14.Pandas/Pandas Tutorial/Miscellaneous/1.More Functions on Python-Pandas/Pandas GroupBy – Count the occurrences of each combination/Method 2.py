new = df.groupby(['States','Products'])['Sale'].count()
display(new)

# Groupby the quality column using aggreate
# value of mean and std
qual = df.groupby("quality").agg([np.mean, np.std])
qual = qual['insert']
qual.plot(kind = "barh", y = "mean", legend = False,
		xerr = "std", title = "Quality", color='green')

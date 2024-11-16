fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax, data = data.iloc[:, 1:3])

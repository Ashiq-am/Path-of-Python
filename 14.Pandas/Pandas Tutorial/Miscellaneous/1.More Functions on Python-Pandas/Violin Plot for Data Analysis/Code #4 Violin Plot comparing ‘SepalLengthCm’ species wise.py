fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax, x = data["Species"],
				y = data["SepalLengthCm"] )

import seaborn as sns


sns.set(style ="ticks")
tips = sns.load_dataset('tips')
markers = {"Lunch": "s", "Dinner": "X"}

ax = sns.scatterplot(x ="total_bill",
					y ="tip",
					style ="time",
					markers = markers,
					data = tips)

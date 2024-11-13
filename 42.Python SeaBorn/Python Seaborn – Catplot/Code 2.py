import seaborn as sns

sns.set_theme(style="ticks")
exercise = sns.load_dataset("exercise")

g = sns.catplot(x="time",
				kind="count",
				data=exercise)

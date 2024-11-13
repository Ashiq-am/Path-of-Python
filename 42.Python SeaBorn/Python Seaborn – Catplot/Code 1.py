import seaborn as sns

exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", y="pulse",
				hue="kind",
				data=exercise)

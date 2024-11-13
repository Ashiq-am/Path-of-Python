import seaborn as sns

exercise = sns.load_dataset("exercise")
g = sns.catplot(x="pulse",
				y="time",
				kind="bar",
				data=exercise)

import seaborn as sns


sns.set(style ="ticks")
tips = sns.load_dataset('tips')

sns.relplot(x ="total_bill",
			y ="tip",
			kind ="scatter",
			data = tips)

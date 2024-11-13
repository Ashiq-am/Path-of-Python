import seaborn as sns


sns.set(style = 'whitegrid')
dots = sns.load_dataset("dots").query("align == 'dots'")

sns.lineplot(x ="time",
			y ="firing_rate",
			hue ="coherence",
			style ="choice",
			data = dots)

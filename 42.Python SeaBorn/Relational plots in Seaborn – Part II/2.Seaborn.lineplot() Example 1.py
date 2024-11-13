import seaborn as sns


sns.set(style = 'whitegrid')
fmri = sns.load_dataset("fmri")

sns.lineplot(x ="timepoint",
			y ="signal",
			data = fmri)

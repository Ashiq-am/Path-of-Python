import seaborn


seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")

seaborn.swarmplot(x="timepoint",
				y="signal",
				hue="region",
				data=fmri)

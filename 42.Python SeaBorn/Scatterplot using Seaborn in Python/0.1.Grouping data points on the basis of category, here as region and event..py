import seaborn


seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")

seaborn.scatterplot(x="timepoint",
					y="signal",
					hue="region",
					style="event",
					data=fmri)

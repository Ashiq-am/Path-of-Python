# Python program to illustrate
# boxplot using inbuilt data-set
# given in seaborn

# importing the required module
import seaborn

# use to set style of background of plot
seaborn.set(style="whitegrid")

# loading data-set
tip = seaborn.load_dataset("fmri")

seaborn.boxplot(x ="timepoint",
			y ="signal",
			hue ="region",
			data = fmri)

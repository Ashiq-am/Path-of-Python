# Python program to illustrate
# violin plot using catplot

# importing the required module
import seaborn

# use to set style of background of plot
seaborn.set(style="whitegrid")

# loading data-set
tips = seaborn.load_dataset("tips")

seaborn.catplot(x="tip", kind="violin", aspect=1.2,
				y="day", data=tips)

# Python program to illustrate
# violinplot using inbuilt data-set
# given in seaborn

# importing the required module
import seaborn

# use to set style of background of plot
seaborn.set(style="whitegrid")

# loading data-set
tips = seaborn.load_dataset("tips")

seaborn.violinplot(x="time", y="tip", data=tips,
				order=["Dinner", "Lunch"])

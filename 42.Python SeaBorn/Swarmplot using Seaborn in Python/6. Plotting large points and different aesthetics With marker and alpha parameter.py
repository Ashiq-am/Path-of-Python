# Python program to illustrate
# swarmplot using inbuilt data-set
# given in seaborn

# importing the required module
import seaborn

# use to set style of background of plot
seaborn.set(style="whitegrid")

# loading data-set
tips = seaborn.load_dataset("tips")

seaborn.swarmplot(x="day", y="total_bill", hue="smoker",
				data=tips, palette="Set2", size=20, marker="D",
				edgecolor="gray", alpha=.25)

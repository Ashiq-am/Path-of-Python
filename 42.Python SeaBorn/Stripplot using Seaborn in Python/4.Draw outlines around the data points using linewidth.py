# Python program to illustrate
# Stripplot using inbuilt data-set
# given in seaborn

# importing the required module
import seaborn
import matplotlib.pyplot as plt

# use to set style of background of plot
seaborn.set(style = 'whitegrid')

# loading data-set
tips = seaborn.load_dataset("tips")

seaborn.stripplot(y="total_bill", x="day", data=tips,
				linewidth=3)

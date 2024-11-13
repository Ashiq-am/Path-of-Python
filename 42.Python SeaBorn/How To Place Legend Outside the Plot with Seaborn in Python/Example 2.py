# set our graph style to whitegrid
sns.set(style="whitegrid")

# load the gammas dataset
ds = sns.load_dataset("gammas")

# use seaborn's lineplot to plot our timeplot
# and BOLD signal columns
sns.lineplot(data=ds, x="timepoint", y="BOLD signal", hue = "ROI")

plt.show()

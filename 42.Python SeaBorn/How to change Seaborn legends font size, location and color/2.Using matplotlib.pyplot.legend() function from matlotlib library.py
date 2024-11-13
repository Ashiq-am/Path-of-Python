# import modules
import seaborn as sns
import matplotlib.pylab as plt
sns.set_style("whitegrid")

# load dataset
tips = sns.load_dataset("tips")

# depict ilustration
gfg = sns.stripplot(x="sex", y="total_bill",
					hue="day", data=tips, jitter=True)
gfg.legend(fontsize=5)
plt.show()

# import modules
import seaborn as sns
import matplotlib.pylab as plt
sns.set_style("whitegrid")

# load dataset
tips = sns.load_dataset("tips")

# depict ilustration
fg = sns.stripplot(x="sex", y="total_bill",
				hue="day", data=tips, jitter=True)

# to chnage the legends location
gfg.legend(bbox_to_anchor= (1.2,1))
plt.show()

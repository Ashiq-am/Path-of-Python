# import modules
import seaborn as sns
import matplotlib.pylab as plt
sns.set_style("whitegrid")

# load dataset
tips = sns.load_dataset("tips")

# depict ilustration
gfg = sns.stripplot(x="sex", y="total_bill",
					hue="day", data=tips, jitter=True)

# for legend text
plt.setp(gfg.get_legend().get_texts(), fontsize='10')

# for legend title
plt.setp(gfg.get_legend().get_title(), fontsize='20')
plt.show()

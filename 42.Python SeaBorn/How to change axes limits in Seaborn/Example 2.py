# import module
import seaborn as sns
sns.set_style("whitegrid")

# assign dataset
tips = sns.load_dataset("tips")

# depict visualization
gfg = sns.boxplot(x="day", y="total_bill",
				data=tips)
gfg.set_ylim(0, 80)

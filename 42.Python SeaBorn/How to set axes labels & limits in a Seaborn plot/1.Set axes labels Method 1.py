# import seaborn
import seaborn as sns
sns.set_style("whitegrid")

# import data
tips = sns.load_dataset("tips")

# plot boxplot
gfg = sns.boxplot(x ="day", y ="total_bill", data = tips)

# add label to the axis and label to the plot
gfg.set(xlabel ="GFG X", ylabel = "GFG Y", title ='some title')

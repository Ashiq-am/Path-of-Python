# import seaborn
import seaborn as sns
sns.set_style("whitegrid")

# load data
tips = sns.load_dataset("tips")

# plot boxplot
gfg = sns.boxplot(x ="day", y ="total_bill", data = tips)
# This will add title to plot
gfg.set_title( "GFG - GFG")

# This will add label to X-axis
gfg.set_xlabel( "GFG X")
# This will add label to Y-axis
gfg.set_ylabel( "GFG Y")

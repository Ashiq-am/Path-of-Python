# importing packages
import seaborn as sb

# load dataset
df = sb.load_dataset('tips')

# perform groupby
df = df.groupby(['size', 'sex']).agg(mean_total_bill=("total_bill", 'mean'))
df = df.reset_index()

# plot barplot
sb.barplot(x="size",
		y="mean_total_bill",
		hue="sex",
		data=df)

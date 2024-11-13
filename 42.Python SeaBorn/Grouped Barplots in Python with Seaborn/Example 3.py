# importing packages
import seaborn as sb

# load dataset
df = sb.load_dataset('anagrams')

# perform groupby
df = df.groupby(['num1', 'attnr']).agg(mean_num3=("num3", 'mean'))
df = df.reset_index()

# plot barplot
sb.barplot(x="num1",
		y="mean_num3",
		hue="attnr",
		data=df)

# importing the library
import seaborn as sns

# selecting style
sns.set(style ="ticks")

# reading the dataset
tips = sns.load_dataset('tips')

sns.relplot(x="total_bill",
			y="tip",
			hue="day",
			size="size",
			data=tips)

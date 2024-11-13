# importing the library
import seaborn as sns

# selecting style
sns.set(style ="ticks")

# reading the dataset
tips = sns.load_dataset('tips')

# plotting a simple visualiation of data points
sns.relplot(x ="total_bill", y ="tip", data = tips)

# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

# class v / s fare barplot in given order
sns.barplot(x = 'class', y = 'fare', data = df,
			order = ["Third", "Second", "First"])

# Show the plot
plt.show()

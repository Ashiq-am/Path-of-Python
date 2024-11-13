# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

# class v / s fare barplot
sns.countplot(x ='sex', data = df,color="salmon", facecolor=(0, 0, 0, 0),
				linewidth=5,
				edgecolor=sns.color_palette("BrBG", 2))
# Show the plot
plt.show()

# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file from seaborn libraray
df = sns.load_dataset('titanic')

# class v / s fare barplot with same colour
sns.barplot(x = 'class', y = 'fare', data = df, color = "salmon")

# Show the plot
plt.show()

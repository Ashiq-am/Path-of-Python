# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

# fare v / s class horizontal barplot
sns.barplot(x = 'fare', y = 'class', hue = 'sex', data = df)

# Show the plot
plt.show()

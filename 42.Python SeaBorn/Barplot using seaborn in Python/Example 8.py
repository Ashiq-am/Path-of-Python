# importing the required library
import seaborn as sns
from numpy import median
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

sns.barplot(x = 'class', y = 'fare', hue = 'sex', data = df, estimator=median)

# Show the plot
plt.show()

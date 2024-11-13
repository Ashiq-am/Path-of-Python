# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')

sns.barplot(x = 'class', y = 'fare',
			hue = 'sex', data = df, palette='pastel')

# Show the plot
plt.show()

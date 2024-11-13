# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# loading diamonds dataset provided by seaborn
diam = sns.load_dataset('diamonds')

# making ECDF plot using displot() on depth
# of the diamonds
sns.displot(data=diam,x='depth',kind='ecdf')

# visualizing the plot using matplotlib.pyplot
# show() function
plt.show()

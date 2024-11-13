# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# loading exercise dataset provided by seaborn
excr = sns.load_dataset('exercise')

# making ECDF plot when we have multiple
# distributions
sns.ecdfplot(data=excr, x='pulse', hue='kind')

# visualizing the plot using matplotlib.pyplot
# show() function
plt.show()

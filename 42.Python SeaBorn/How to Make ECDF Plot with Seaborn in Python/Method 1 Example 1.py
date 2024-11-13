# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# loading exercise dataset provided by seaborn
excr = sns.load_dataset('exercise')

# making ECDF plot
sns.ecdfplot(data=excr,x='pulse')

# visualizing the plot using matplotlib.pyplot
# show() function
plt.show()

# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# importing iris dataset from the library
df2 = sns.load_dataset('iris')

# plotting histogram and density plot for
# sepal width using distplot() by setting color
sns.distplot(a=df2.sepal_width, color='red',
			hist_kws={"edgecolor": 'white'})

# visualizing plot using matplotlib.pyplot library
plt.show()

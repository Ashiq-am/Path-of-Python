# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# importing iris dataset from the library
df2 = sns.load_dataset('iris')

# plotting histogram and density plot for
# petal length using distplot() by setting color
sns.distplot(a=df2.petal_length, color='green',
			hist_kws={"edgecolor": 'black'})

# visualizing plot using matplotlib.pyplot library
plt.show()

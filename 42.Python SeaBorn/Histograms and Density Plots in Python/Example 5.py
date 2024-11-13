# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# importing diamond dataset from the library
df = sns.load_dataset('diamonds')

# plotting histogram and density plot
# for carat using distplot() by setting color
sns.distplot(a=df.carat, bins=40, color='purple',
			hist_kws={"edgecolor": 'black'})

# visualizing plot using matplotlib.pyplot library
plt.show()

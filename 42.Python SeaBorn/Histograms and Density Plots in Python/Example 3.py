# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# importing diamond dataset from the library
df = sns.load_dataset('diamonds')

# plotting density plot for carat using distplot()
sns.distplot(a=df.carat, hist=False)

# visualizing plot using matplotlib.pyplot library
plt.show()

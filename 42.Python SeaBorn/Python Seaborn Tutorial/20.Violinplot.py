# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.violinplot(x='species', y='sepal_width', data=data)
plt.show()

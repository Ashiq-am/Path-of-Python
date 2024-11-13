# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.barplot(x='species', y='sepal_length', data=data)
plt.show()

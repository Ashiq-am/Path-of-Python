# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.lineplot(x='sepal_length', y='species', data=data)
plt.show()

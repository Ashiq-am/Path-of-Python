# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# crrating the relplot
sns.relplot(x='sepal_width', y='species', data=data)

plt.show()

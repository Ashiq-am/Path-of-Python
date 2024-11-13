# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

sns.regplot(x='total_bill', y='tip', data=data)
plt.show()

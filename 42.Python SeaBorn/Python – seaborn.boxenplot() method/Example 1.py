# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# plot the boxenplot
sns.boxenplot(x = "day", y = "total_bill",
			data = data)
plt.show()

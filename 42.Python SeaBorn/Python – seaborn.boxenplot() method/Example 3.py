# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# plot the boxenplot
# orient to horizontal
sns.boxenplot(x = "total_bill", y = "size",
			data = data, orient ="h")
plt.show()

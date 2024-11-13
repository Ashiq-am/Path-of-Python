# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# draw pointplot
sns.pointplot(x = "size",
			y = "total_bill",
			linestyles = '-.',
			markers = '^',
			hue = "sex",
			data = data)
# show the plot
plt.show()


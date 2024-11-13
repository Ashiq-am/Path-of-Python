# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# draw pointplot with
# hue = smoker
sns.pointplot(x = "sex",
			y = "total_bill",
			hue = "smoker",
			data = data)
# show the plot
plt.show()

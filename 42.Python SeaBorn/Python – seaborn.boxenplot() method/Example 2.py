# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# plot the boxenplot
# hue by sex
# width of 0.8
sns.boxenplot(x ="day", y = "total_bill", hue = "sex",
			data = data, width = 0.8)
plt.show()

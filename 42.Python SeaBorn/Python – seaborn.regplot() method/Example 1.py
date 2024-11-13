# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("mpg")

# draw regplot
sns.regplot(x = "mpg",
			y = "acceleration",
			data = data)

# show the plot
plt.show()


# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("titanic")

# draw regplot
sns.regplot(x = "age",
			y = "fare",
			data = data,
			dropna = True)
# show the plot
plt.show()



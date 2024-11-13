# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("mpg")

# draw jointplot with
# scatter kind
sns.jointplot(x = "mpg", y = "acceleration",
			kind = "scatter", data = data)
# show the plot
plt.show()

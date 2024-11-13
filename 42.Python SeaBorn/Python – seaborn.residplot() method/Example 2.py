# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw residplot
# with lowess = True
sns.residplot(x = "petal_length",
			y = "petal_width",
			data = data,
			lowess = True)

# show the plot
plt.show()



# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("titanic")

# draw jointplot with
# reg kind
sns.jointplot(x = "age", y = "fare",
			kind = "reg", data = data,
			dropna = True)

# show the plot
plt.show()


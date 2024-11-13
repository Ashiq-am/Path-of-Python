# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("attention")

# draw jointplot with
# hex kind
sns.jointplot(x = "solutions", y = "score",
			kind = "hex", data = data)
# show the plot
plt.show()


# importing required packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("attention")

# draw regplot
sns.regplot(x = "solutions",
			y = "score",
			data = data)

# show ther plot
plt.show()


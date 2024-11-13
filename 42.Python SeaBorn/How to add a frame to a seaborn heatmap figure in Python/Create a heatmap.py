# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing dataset
example = sns.load_dataset("flights")
example = example.pivot("month", "year",
						"passengers")

# Creating plot
res = sns.heatmap(example)

# show plot
plt.show()

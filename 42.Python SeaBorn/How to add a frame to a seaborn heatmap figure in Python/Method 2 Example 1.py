# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing dataset
example = sns.load_dataset("flights")
example = example.pivot("month", "year",
						"passengers")

# Creating plot
res = sns.heatmap(example, cmap = "Purples")

# Drawing the frame
for _, spine in res.spines.items():
	spine.set_visible(True)
	spine.set_linewidth(5)

# show plot
plt.show()

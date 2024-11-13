# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing dataset
example = sns.load_dataset("flights")
example = example.pivot("month", "year",
						"passengers")

# Creating plot
res = sns.heatmap(example, cmap = "BuPu")

# Drawing the frame
res.axhline(y = 0, color='k',linewidth = 10)
res.axhline(y = example.shape[1], color = 'k',
			linewidth = 10)

res.axvline(x = 0, color = 'k',
			linewidth = 10)

res.axvline(x = example.shape[0],
			color = 'k', linewidth = 10)

# show plot
plt.show()

# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Preparing dataset
example = np.random.rand(10, 12)

# Creating plot
res = sns.heatmap(example, cmap = "Greens",
				linewidths = 2,
				linecolor = "white")

# Drawing the frame
for _, spine in res.spines.items():
	spine.set_visible(True)
	spine.set_linewidth(3)
	spine.set_linestyle("dashdot")

# show plot
plt.show()

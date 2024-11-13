# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Preparing dataset
example = np.random.rand(10, 12)

# Creating plot
res = sns.heatmap(example, cmap = "magma",
				linewidths = 0.5)

# Drawing the frame
res.axhline(y = 0, color = 'k',
			linewidth = 15)

res.axhline(y = 10, color = 'k',
			linewidth = 15)

res.axvline(x = 0, color = 'k',
			linewidth = 15)

res.axvline(x = 12, color = 'k',
			linewidth = 15)
# show plot
plt.show()

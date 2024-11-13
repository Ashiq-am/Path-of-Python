import seaborn as sns
import numpy as np


np.random.seed(0)

data = np.random.rand(12, 12)
ax = sns.heatmap(data, cmap="PiYG")

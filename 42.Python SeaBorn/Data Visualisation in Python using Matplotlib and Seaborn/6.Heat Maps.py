# import required module
import seaborn as sns
import numpy as np

# assign data
data = np.random.randn(50, 20)

# illustrate heat map
ax = sns.heatmap(data, xticklabels=2, yticklabels=False)

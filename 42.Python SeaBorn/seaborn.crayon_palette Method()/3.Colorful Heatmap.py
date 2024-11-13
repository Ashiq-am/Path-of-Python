import numpy as np
import seaborn as sns

np.random.seed(0)
data = np.random.rand(10, 10)

palette = sns.crayon_palette(['Red', 'Blue', 'Green', 'Yellow', 'Orange'])

sns.heatmap(data, cmap=palette, cbar=True)
plt.show()

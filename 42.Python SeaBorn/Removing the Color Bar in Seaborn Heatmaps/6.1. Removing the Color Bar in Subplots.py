import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(12,10)
fig, axs = plt.subplots(1, 2, figsize=(8,3))

# Heatmap with color bar
sns.heatmap(data, ax=axs[0], cbar=True)
axs[0].set_title('With Color Bar')

# Heatmap without color bar
sns.heatmap(data, ax=axs[1], cbar=False)
axs[1].set_title('Without Color Bar')

plt.show()

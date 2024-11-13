import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.rand(10, 12)
data2 = np.random.rand(10, 12)

# Define the overall maximum for normalization
overall_max = max(data1.max(), data2.max())

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.heatmap(data1, vmax=overall_max, cmap="Blues")
plt.title("Heatmap 1")

plt.subplot(1, 2, 2)
sns.heatmap(data2, vmax=overall_max, cmap="Blues")
plt.title("Heatmap 2")

plt.tight_layout()
plt.show()

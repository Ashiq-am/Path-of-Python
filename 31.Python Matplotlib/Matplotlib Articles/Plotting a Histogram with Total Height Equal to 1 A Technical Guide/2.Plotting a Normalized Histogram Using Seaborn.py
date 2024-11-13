import seaborn as sns
import numpy as np

data = np.random.randn(1000)
sns.histplot(data, bins=30, kde=False, stat='density', color='blue', alpha=0.6)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram (Total Height Equals 1)')
plt.show()

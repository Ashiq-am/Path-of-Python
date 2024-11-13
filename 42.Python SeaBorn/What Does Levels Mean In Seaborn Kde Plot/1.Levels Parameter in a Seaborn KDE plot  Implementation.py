import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some random bivariate data
data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], size=300)

# Create a KDE plot with specified levels
sns.kdeplot(x=data[:, 0], y=data[:, 1], levels=[0.1, 0.5, 0.9], cmap="Blues")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a sample dataset
np.random.seed(10)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)
data = pd.DataFrame({'x': x, 'y': y})

# Compute custom error values
error = np.random.normal(0.1, 0.02, size=y.shape)
lower = y - error
upper = y + error

# Plot the lineplot
ax = sns.lineplot(x='x', y='y', data=data)

# Add custom error bars using fill_between
ax.fill_between(x, lower, upper, color='b', alpha=0.2)

plt.show()

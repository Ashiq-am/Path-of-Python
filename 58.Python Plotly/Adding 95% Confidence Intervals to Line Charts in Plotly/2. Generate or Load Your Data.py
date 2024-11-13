import numpy as np

# Generate synthetic data
np.random.seed(0)
x = np.arange(2000, 2025)
y = np.random.normal(loc=0, scale=1, size=len(x)).cumsum()
ci_upper = y + 1.96 * np.std(y) / np.sqrt(len(y))
ci_lower = y - 1.96 * np.std(y) / np.sqrt(len(y))

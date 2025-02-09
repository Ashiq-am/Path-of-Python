from scipy import stats
import numpy as np

# Generating random data
data = np.random.normal(loc=0, scale=1, size=1000)

# Performing a statistical test
z_score = stats.zscore(data)
print("Z-scores:\n", z_score)
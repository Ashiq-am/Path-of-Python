import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Create a basic violin plot
plt.violinplot(data)
plt.show()

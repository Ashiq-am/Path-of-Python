import matplotlib.pyplot as plt
import numpy as np

# Sample data with NaN values
data = [np.random.normal(0, std, 100).tolist() for std in range(1, 4)]
data[1][10:15] = [np.nan] * 5  # Introducing NaNs in the second group

# Create a boxplot
plt.boxplot(data)
plt.title('Boxplot with NaN Values')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.normal(100, 10, 200)

# Create a boxplot
plt.boxplot(data)
plt.title('Single Boxplot')
plt.show()

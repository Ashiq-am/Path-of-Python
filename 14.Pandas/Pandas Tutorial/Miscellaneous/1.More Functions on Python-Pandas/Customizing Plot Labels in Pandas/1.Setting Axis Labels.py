import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [10, 15, 13, 18, 20]}
df = pd.DataFrame(data)

# Create a scatter plot with custom axis labels
ax = df.plot(kind='scatter', x='x', y='y')
ax.set_xlabel('Custom X Label')
ax.set_ylabel('Custom Y Label')
plt.show()

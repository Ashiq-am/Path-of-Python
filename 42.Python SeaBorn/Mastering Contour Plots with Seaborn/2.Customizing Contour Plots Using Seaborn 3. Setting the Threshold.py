import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)

# Create a contour plot
plt.figure(figsize=(6, 6))
sns.kdeplot(x=x, y=y, fill=True, cmap="viridis", thresh=0.1, levels=100)
plt.title('Contour Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

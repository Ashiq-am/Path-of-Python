import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Customized Gridlines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# Customizing gridlines
plt.grid(color='blue', linestyle='-.', linewidth=1.5, alpha=0.7)
plt.show()
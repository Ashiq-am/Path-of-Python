import numpy as np
import matplotlib.pyplot as plt

# Creating sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# Creating the contour plot
plt.contour(X, Y, Z, levels=10, cmap='viridis')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Contour Plot')

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a basic plot
plt.plot(x, y1, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave')
plt.title('Basic Plot with Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

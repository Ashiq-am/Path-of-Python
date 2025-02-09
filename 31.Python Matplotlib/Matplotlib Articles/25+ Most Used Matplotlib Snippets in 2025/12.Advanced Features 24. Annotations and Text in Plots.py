import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Adding an annotation
plt.annotate('Local Max', xy=(1.57, 1), xytext=(3, 0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.title('Sine Wave with Annotation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
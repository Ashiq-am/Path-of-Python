import matplotlib.pyplot as plt
import numpy as np

# First figure
plt.figure(1)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
plt.plot(x, y1)
plt.title("I am Figure 1")
plt.show()

# Second figure
plt.figure(2)
y2 = np.cos(x)
plt.plot(x, y2)
plt.title("I am Figure 2")
plt.show()
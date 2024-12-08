import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# First figure: Plotting the sine wave
plt.figure(1)
plt.plot(x, y1)
plt.title("Sine Wave - Figure 1")
plt.show()

# Second figure: Plotting the cosine wave
plt.figure(2)
plt.plot(x, y2)
plt.title("Cosine Wave - Figure 2")
plt.show()
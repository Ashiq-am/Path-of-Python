import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y1)
ax1.set_title("Sine Wave")

ax2.plot(x, y2)
ax2.set_title("Cosine Wave")

plt.show()
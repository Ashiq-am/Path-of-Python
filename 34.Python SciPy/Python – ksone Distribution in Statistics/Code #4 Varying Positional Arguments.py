import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = ksone.pdf(x, 1, 3)
y2 = ksone.pdf(x, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")

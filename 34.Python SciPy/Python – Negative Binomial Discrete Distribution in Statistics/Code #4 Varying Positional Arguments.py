import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = nbinom.ppf(x, a, b)
y2 = nbinom.pmf(x, a, b)
plt.plot(x, y1, "*", x, y2, "r--")

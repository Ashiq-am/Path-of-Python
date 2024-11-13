import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

# Varying positional arguments
y1 = erlang.pdf(x, 2, 6)
y2 = erlang.pdf(x, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")

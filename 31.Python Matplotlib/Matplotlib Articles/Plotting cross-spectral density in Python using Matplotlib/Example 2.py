import numpy as np
import matplotlib.pyplot as plt


t = np.arange(5, 10, 0.25)
ampl = np.sin(t)

plt.plot(t, ampl)
plt.title("Signal 2")

plt.show()

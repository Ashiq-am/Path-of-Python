import numpy as np
import matplotlib.pyplot as plt

plt.vlines(4, 0, 5, linestyles ="dotted", colors ="k")
plt.vlines(3, 0, 5, linestyles ="solid", colors ="k")
plt.vlines(5, 0, 5, linestyles ="dashed", colors ="k")

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.show()

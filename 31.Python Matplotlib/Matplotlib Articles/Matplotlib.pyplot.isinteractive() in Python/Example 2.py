# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

plt.plot(t, s)
plt.ylim(1, 0)
plt.ylabel('Display Y-axis Label', fontweight='bold')
plt.grid(True)

w = plt.isinteractive()

print("Is we can redraw after every plotting command : ",
      str(w))

plt.title('matplotlib.pyplot.isinteractive() function \
Example', fontweight="bold")

plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = np.power(x, 2)
y2 = np.power(x, 3)

fig, ax = plt.subplots()

ax.plot(x, y1, c = 'r',label = '_nolegend_')
ax.plot(x, y2,c = 'g',label = '_nolegend_')

leg = plt.legend()

plt.show()

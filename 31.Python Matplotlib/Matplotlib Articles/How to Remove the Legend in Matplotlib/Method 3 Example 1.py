import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1,c = 'r',label = 'Sine')
ax.plot(x, y2,c = 'g',label = 'Cosine')
leg = plt.legend()
ax.legend_ = None

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x,y)

plt.text(3.5, 0.9, 'Sine wave', fontsize = 23)

plt.xlabel('X-axis', fontsize = 15)
plt.ylabel('Y-axis', fontsize = 15)

#plt.grid(True, which='both')
plt.show()

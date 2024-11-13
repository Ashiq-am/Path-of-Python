# import required modules
import numpy as np
import matplotlib.pyplot as plt

# assign coordinates
x = np.linspace(-np.pi, np.pi, 100)
y = 2*np.sin(x)

# depict illustration
plt.xlim(-np.pi, np.pi)
plt.plot(x, y)
plt.grid(True)
plt.show()

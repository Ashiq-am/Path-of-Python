# import required modules
import numpy as np
import matplotlib.pyplot as plt

# assign coordinates
x = np.linspace(-np.pi, np.pi, 100)
y = 2*np.sin(x)

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# depict illustration
plt.xlim(-np.pi, np.pi)
plt.plot(x, y)
plt.grid(True)
plt.show()

# importing packages
import matplotlib.pyplot as plt
import numpy as np

# making subplots objects
fig, ax = plt.subplots(2, 2)

# create data
x = np.linspace(0, 10, 1000)

# draw graph
ax[0, 0].plot(x, np.sin(x), 'r-.')
ax[0, 1].plot(x, np.cos(x), 'g--')
ax[1, 0].plot(x, np.tan(x), 'y-')
ax[1, 1].plot(x, np.sinc(x), 'c.-')

plt.show()

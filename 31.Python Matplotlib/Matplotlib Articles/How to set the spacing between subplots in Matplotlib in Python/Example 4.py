# importing packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x=np.array([1, 2, 3, 4, 5])

# making subplots with constrained_layout=True
fig, ax = plt.subplots(2, 2,
					constrained_layout = True)

# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
plt.show()

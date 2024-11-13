# importing packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x=np.array([1, 2, 3, 4, 5])

# making subplots
fig, ax = plt.subplots(2, 2)

# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)

# set the spacing between subplots
plt.subplots_adjust(left=0.1,
					bottom=0.1,
					right=0.9,
					top=0.9,
					wspace=0.4,
					hspace=0.4)
plt.show()

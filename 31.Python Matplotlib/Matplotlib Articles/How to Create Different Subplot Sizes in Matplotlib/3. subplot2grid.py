# importing required library
import matplotlib.pyplot as plt
import numpy as np

# creating grid for subplots
fig = plt.figure()
fig.set_figheight(6)
fig.set_figwidth(6)

ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3)
ax2 = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=1)
ax3 = plt.subplot2grid(shape=(3, 3), loc=(1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1)


# initializing x,y axis value
x = np.arange(0, 10, 0.1)
y = np.cos(x)

# plotting subplots
ax1.plot(x, y)
ax1.set_title('ax1')
ax2.plot(x, y)
ax2.set_title('ax2')
ax3.plot(x, y)
ax3.set_title('ax3')
ax4.plot(x, y)
ax4.set_title('ax4')
ax5.plot(x, y)
ax5.set_title('ax5')

# automatically adjust padding horizontally
# as well as vertically.
plt.tight_layout()

# display plot
plt.show()

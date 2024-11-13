# import required modules
import numpy as np
import matplotlib.pyplot as plt

# adjust coordinates
x = y = [i for i in range(0, 6)]

# depict illustartion
fig = plt.figure()
ax = fig.add_subplot()
plt.plot(x, y)

# square plot
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
plt.show()

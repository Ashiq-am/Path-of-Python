# importing numpy as np
import numpy as np

# importig pyplot as plt
import matplotlib.pyplot as plt

# position
pos = 0

# scale
scale = 10

# size
size = 10000


# random seed
np.random.seed(10)

# creating a normal destribution data
values = np.random.normal(pos, scale, size)

# plotting histograph
plt.hist(values, 100)

# plotting mean line
plt.axvline(values.mean(), color='k', linestyle='dashed', linewidth=2)

# showing the plot
plt.show()

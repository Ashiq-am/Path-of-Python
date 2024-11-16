# importing numpy as np
import numpy as np

# importig pyplot as plt
import matplotlib.pyplot as plt

# position
pos = 100
# scale
scale = 5

# size
size = 100000

# creating a normal destribution data
values = np.random.normal(pos, scale, size)

# plotting histograph
plt.hist(values, 100)

# showing hte graph
plt.show()

# import numpy
import numpy as np
import matplotlib.pyplot as plt

gfg = np.arange(16).reshape((4, 4))
# Using shuffle() method
np.random.shuffle(gfg)

print(gfg)

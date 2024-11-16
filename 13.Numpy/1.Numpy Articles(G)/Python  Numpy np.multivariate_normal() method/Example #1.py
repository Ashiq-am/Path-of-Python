# import numpy
import numpy as np

mean = [1, 2]
matrix = [[5, 0], [0, 5]]
# using np.multinomial() method
gfg = np.random.multivariate_normal(mean, matrix, 10)

print(gfg)

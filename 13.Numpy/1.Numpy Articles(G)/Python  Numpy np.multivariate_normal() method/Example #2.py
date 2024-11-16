# import numpy
import numpy as np

mean = [0, 0, 0]
matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# using np.multinomial() method
gfg = np.random.multivariate_normal(mean, matrix, 5)

print(gfg)

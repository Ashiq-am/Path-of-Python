# import numpy
import numpy as np

# using np.char.endswith() method
a = np.array([['geeks', 'for', 'geeks'], ['jitender', 'author', 'gfg']])
gfg = np.char.endswith(a, 'r')

print(gfg)

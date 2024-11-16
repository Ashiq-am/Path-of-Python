# importing the module
import numpy as np

# creating an array
from IPython.core.display import display

gfg = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
display(gfg)

# using resize()
print("Changed array")
# this will print nothing as None is returned
display(gfg.resize(2, 3))

print("Original array:")
display(gfg)

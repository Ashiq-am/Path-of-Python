# importing the module
import numpy as np

# creating an array
from Tools.scripts.dutree import display

gfg = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
display(gfg)

# using reshape()
print("Changed array")
display(gfg.reshape(2, 3))

print("Original array:")
display(gfg)

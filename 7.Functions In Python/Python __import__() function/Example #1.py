# importing numpy module
# it is equivalent to "import numpy"
np = __import__('numpy', globals(), locals(), [], 0)

# array from numpy
a = np.array([1, 2, 3])

# prints the type
print(type(a))

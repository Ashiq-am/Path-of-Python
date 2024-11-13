#import ctypes
import ctypes

# variable declaration
val = 20

# get the memory address of the python
# object for variable
print(id(val))

# get the memory address of the python
# object for list
print(id([1, 2, 3, 4, 5]))

# get the memory address of the python
# object for tuple
print(id((1, 2, 3, 4, 5)))

# get the memory address of the python
# object for set
print(id({1, 2, 3, 4, 5}))

#import ctypes
import ctypes

# variable declaration
val = 20

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

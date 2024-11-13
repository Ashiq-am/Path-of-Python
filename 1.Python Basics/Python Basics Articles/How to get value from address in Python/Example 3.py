#import ctypes
import ctypes


# variable declaration
val = [1, 2, 3, 4, 5]

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable list
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

print("____________________________________")

# variable declaration
val = (1, 2, 3, 4, 5)

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable tuple
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

print("____________________________________")

# variable declaration
val = {1, 2, 3, 4, 5}

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable set
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

print("____________________________________")

# variable declaration
val = {'id': 1, "name": "sravan kumar", "address": "kakumanu"}

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable dictionary
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

print("____________________________________")

import numpy as np


# list
list1 = [1, 2, 3]
print(type(list1))
print(list1)
print()

# conversion
array1 = np.array(list1)
print(type(array1))
print(array1)
print()

# tuple
tuple1 = ((1, 2, 3))
print(type(tuple1))
print(tuple1)
print()

# conversion
array2 = np.array(tuple1)
print(type(array2))
print(array2)
print()

# list, array and tuple
array3 = np.array([tuple1, list1, array2])
print(type(array3))
print(array3)

# Python Program illustrating
# numpy.tile()

import numpy as geek

arr = geek.arange(4).reshape(2, 2)
print("arr : \n", arr)

a = 2
b = 1
repetitions = (a, b)
print("\nRepeating arr : \n", geek.tile(arr, repetitions))
print("arr Shape : \n", geek.tile(arr, repetitions).shape)

a = 3
b = 2
repetitions = (a, b)
print("\nRepeating arr : \n", geek.tile(arr, repetitions))
print("arr Shape : \n", geek.tile(arr, repetitions).shape)

a = 2
b = 3
repetitions = (a, b)
print("\nRepeating arr : \n", geek.tile(arr, repetitions))
print("arr Shape : \n", geek.tile(arr, repetitions).shape)

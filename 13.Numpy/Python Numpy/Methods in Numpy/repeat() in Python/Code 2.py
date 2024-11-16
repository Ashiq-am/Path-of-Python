# Python Program illustrating
# numpy.repeat()

import numpy as geek

arr = geek.arange(6).reshape(2, 3)
print("arr : \n", arr)

repetitions = 2
print("\nRepeating arr : \n", geek.repeat(arr, repetitions, 1))
print("arr Shape : \n", geek.repeat(arr, repetitions).shape)

repetitions = 2
print("\nRepeating arr : \n", geek.repeat(arr, repetitions, 0))
print("arr Shape : \n", geek.repeat(arr, repetitions).shape)

repetitions = 3
print("\nRepeating arr : \n", geek.repeat(arr, repetitions, 1))
print("arr Shape : \n", geek.repeat(arr, repetitions).shape)

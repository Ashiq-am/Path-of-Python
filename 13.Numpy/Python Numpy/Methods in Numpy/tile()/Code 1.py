# Python Program illustrating
# numpy.tile()

import numpy as geek

#Working on 1D
arr = geek.arange(5)
print("arr : \n", arr)

repetitions = 2
print("Repeating arr 2 times : \n", geek.tile(arr, repetitions))

repetitions = 3
print("\nRepeating arr 3 times : \n", geek.tile(arr, repetitions))
# [0 1 2 ..., 2 3 4] means [0 1 2 3 4 0 1 2 3 4 0 1 2 3 4]
# since it was long output, so it uses [ ... ]

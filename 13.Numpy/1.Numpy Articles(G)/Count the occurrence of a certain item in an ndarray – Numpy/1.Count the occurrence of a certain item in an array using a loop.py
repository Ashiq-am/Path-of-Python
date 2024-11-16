import numpy as np

arr = np.array([2, 3, 4, 5, 3, 3,
                5, 4, 7, 8, 3])

print('Numpy Array:')
print(arr)
c = 0
element = 3

for j in arr:
    if j == element:
        c += 1

print("element occurred", c, "times")

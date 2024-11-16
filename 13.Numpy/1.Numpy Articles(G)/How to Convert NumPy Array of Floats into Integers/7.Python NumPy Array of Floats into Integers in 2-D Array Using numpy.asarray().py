import numpy as np

org = np.array([
    [1.2, 2.3, 3.4],
    [0.1, 1.3, 2.6],
    [1.5, 4.5, 9.2]])

# displaying the original array
print("Original Array : ")
print(org, "\n")

# applying .asarray() with dtype (data type) as integer
integer = np.asarray(org, dtype=int)

# displaying the integer array

print("Integer Array : ")
print(integer)

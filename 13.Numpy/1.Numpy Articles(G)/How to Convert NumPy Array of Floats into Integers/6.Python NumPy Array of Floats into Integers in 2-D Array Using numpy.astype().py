import numpy as np

org = np.array([
    [1.2, 2.3, 3.4],
    [0.1, 1.3, 2.6],
    [1.5, 4.5, 9.2]])

# displaying the original array
print("Original Array : ")
print(org, "\n")

# applying .astype()
integer = org.astype(int)

# displaying the integer array

print("Integer Array : ")
print(integer)

import numpy as np

org = np.array([
    [1.2, 2.3, 3.4],
    [0.1, 1.3, 2.6],
    [1.5, 4.5, 9.2]])

# displaying the original array
print("Original Array : ")
print(org, "\n")

# Create an empty list
new = []

for i in range(org.shape[0]):
    helper = []
    for j in range(org.shape[1]):
        helper.append(int(org[i, j]))
    new.append(helper)

integer = np.array(new)

# displaying the integer array

print("Integer Array : ")
print(integer)

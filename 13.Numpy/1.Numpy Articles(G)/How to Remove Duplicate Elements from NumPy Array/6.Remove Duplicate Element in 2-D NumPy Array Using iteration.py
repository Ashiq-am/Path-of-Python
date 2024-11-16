import numpy as np

org = np.array([
    [1, 2, 3, 4, 5],
    [0, 1, 2, 9, 8],
    [1, 4, 9, 8, 5],
    [1, 2, 3, 4, 5],
    [0, 1, 2, 9, 8]])

# displaying the original array
print("Original Array : ")
print(org, "\n")

new = []  # defining a new array

# iterating through each element of org array
for i in org:
    if list(i) not in new:
        new.append(list(i))

new = np.array(new)

# displaying the new array with updated/unique elements
print("New Array : ")
print(new)

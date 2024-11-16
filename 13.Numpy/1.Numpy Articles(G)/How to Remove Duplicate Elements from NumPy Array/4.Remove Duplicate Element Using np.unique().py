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

new = [list(i) for i in org]
# using the .unique() with axis=0
new = np.unique(new, axis=0)

# displaying the new array with updated/unique elements
print("New Array : ")
print(new)

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

# Convert each row of original array to a frozenset
rows = set()
for i in org:
    rows.add(frozenset(i))

# Convert the frozensets back to NumPy array
new = np.array([list(i) for i in rows])

# displaying the new array with updated/unique elements
print("New Array : ")
print(new)

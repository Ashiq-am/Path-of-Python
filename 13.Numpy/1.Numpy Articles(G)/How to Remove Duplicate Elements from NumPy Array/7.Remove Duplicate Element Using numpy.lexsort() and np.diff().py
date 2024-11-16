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

new = np.lexsort(org.T)  # pssing transpose of org array to lexsort()

new01 = org[new, :]
# it gets the indices value given by "new array" and create a new01 array

x = np.concatenate(([True], np.any(np.diff(new01, axis=0), axis=1)))
result = np.array(new01[x])

# displaying the new array with updated/unique elements
print("Result Array : ")
print(result)

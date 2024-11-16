import numpy as np

#declaring original array
org = np.array([1, 2, 3, 4, 5, 1, 2, 3, 1, 2 , 9])

#displaying the original array
print("Original Array : ")
print(org,"\n")

#using the set operation
new = set(org)
new = np.array(list(new))

#displaying the new array with updated/unique elements
print("New Array : ")
print(new)

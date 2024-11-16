import numpy as np

#declaring original array
org = np.array([1, 2, 3, 4, 5, 1, 2, 3, 1, 2 , 9])

#displaying the original array
print("Original Array : ")
print(org,"\n")

l = []
for i in org:
	if i not in l:
		l.append(i)

new = np.array(l)

#displaying the new array with updated/unique elements
print("New Array : ")
print(new)

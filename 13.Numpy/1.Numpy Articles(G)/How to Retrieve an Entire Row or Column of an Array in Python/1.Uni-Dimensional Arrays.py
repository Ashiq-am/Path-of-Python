# importing the required package
import numpy as np

# creating a numpy character array
arr1 = np.array(["Ram", "Shyam" , "Sita"])

print("First row - ")
print(arr1)

# printing first column referred by first index
print ("First Column")
print (arr1[0])

# computing length of array
length = len(arr1)
print("Last Column")
print (arr1[length-1])

import numpy as np

#creating the original array
org = [1.2,4.5,9.1,6.5,8.9,2.3,1.2]
org = np.array(org)

#Displaying the original array
print("Original Array : ")
print(org,"\n")

#converting the array to its integer form
new = np.asarray(org,dtype="int")

#Displaying the result
print("New Array : ")
print(new)

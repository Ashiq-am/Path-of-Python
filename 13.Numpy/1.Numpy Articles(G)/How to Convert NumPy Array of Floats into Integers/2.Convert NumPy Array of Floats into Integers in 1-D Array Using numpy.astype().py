import numpy as np

org = [1.2,3.4,5.6,7.8,9.1,11.2,14.5,16.7]
org = np.array(org)

print("Original Array : ")
print(org,"\n")

#Just eliminating the integer part
integer_array = org.astype(int)

#Displaying the result
print("Integer Array : ")
print(integer_array,"\n")

#converting for closest integer value
round_array = np.round(org).astype(int)

#Displaying the result
print("Round Array : ")
print(round_array)

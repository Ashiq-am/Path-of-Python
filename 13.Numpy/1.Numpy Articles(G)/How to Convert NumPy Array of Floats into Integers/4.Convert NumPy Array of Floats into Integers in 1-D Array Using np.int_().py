import numpy as np

#creating the original array
org = [1.2,4.5,9.1,6.7,8.9,2.8,1.7]
org = np.array(org)

#Displaying the original array
print("Original Array : ")
print(org,"\n")

#Just eliminating the integer part
integer_array = np.int_(org)

#Displaying the result
print("Integer Array : ")
print(integer_array,"\n")

#converting for closest integer value
round_array = np.round_(org)
round_array = np.int_(round_array)

#Displaying the result
print("Round Array : ")
print(round_array)

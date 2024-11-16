import numpy as np

org = np.array([1.2,3.4,5.6,7.8,9.1,11.2,14.5,16.7])

#Displaying the original array
print("Original Array : ")
print(org,"\n")

#coverting array's float value to its integer value using int()
integer_array = np.array([int(i) for i in org])

#Displaying the result
print("Integer Array : ")
print(integer_array,"\n")

#coverting array's float value to its integer value using round()
round_array = np.array([round(i) for i in org])

#Displaying the result
print("Round Array : ")
print(round_array)

# Program to fetch particular
# elements of structure


import time


# Creating dictionary and list
dict_name ={"bob":12, "john":11}
list_name =[2, 3, 4, 5, 1]

# Time taken by dictionary
x = time.time()
L = dict_name["bob"]
y = time.time()
print("Time taken by dictionary:", y-x)

# Time taken by list
x = time.time()
L = list_name[2]
y = time.time()
print("\nTime taken by list:", y-x)

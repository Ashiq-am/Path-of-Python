# Python program to demonstrate
# that elements of list and array can
# be accessed through index and iteration

# importing array module
import array as arr

# Declaring a list
List1 = [10, 20, 30, 20, 10, 40]

# Printing the list
print("List1 elements: ", List1, "\n")

# Accessing elements of list by index number
print("Element at index 0: ", List1[0])
print("Element at index 1: ", List1[1])
print("Element at index 3: ", List1[3])
print("Element at index 4: ", List1[4])

# Accessing elements of the list
# using negative indexing

# Printing last element of the list
print("Element at last index: ", List1[-1])

# Printing 3rd last
# the element of the list
print("Element at " \
      "3rd last index: ", List1[-3])

# Accessing elements of list through iteration
print("Accessing through iteration: ", end=" ")
for item in range(len(List1)):
    print(List1[item], end=" ")

# Declaring an array
Array1 = arr.array('i', \
                   [10, 20, 30, 40, 50, 60])
print("\nArray1: ", Array1)

# Accessing the elements of an array

# Access element of
# array by index number
print("Element of Array1"" at index 3: ", Array1[3])

# Accessing elements of
# array through iteration
print("Accessing through iteration:"" ", end=" ")
for i in range(len(Array1)):
    print(Array1[i], end=" ")

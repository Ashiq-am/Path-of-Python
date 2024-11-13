# Python program to demonstrate
# both the list and array is mutable

# importing array module
import array as arr

# Declaring a list
List1 = ["Geeks", 1, "Geeks"]

# Printing original list
print("Original list: ", List1)

# Changing the value of the
# element at a specific index
List1[1] = "for"

# Printing modified list
print("\nModified list: ", List1)

# Declaring an array with integers values
Array1 = arr.array('i',[10, 20, 30, 37, 50, ])

# Printing original array
print("\nOriginal array: ", end=" ")
for i in range(len(Array1)):
    print(Array1[i], end=" ")

# Updating an element in the array
Array1[3] = 40

# Printing modified Array:
print("\nModified array: ", end="")
for i in range(len(Array1)):
    print(Array1[i], end=" ")

# Python program to demonstrate
# some operations on arrays

# importing array module
import array as arr

# declaring an array of integer type
# 'i' signifies integer type and
# elements inside [] are the array elements
a1 = arr.array('i', [10, 20, 30])

# printing array with
# data type and elements
print("Array a1: ", a1)

# printing elements of array
print("Elements of the array" \
      "a1 is : ", end=" ")
for i in range(len(a1)):
    print(a1[i], end=", ")
print()

# Declaring an array of float type
# 'd' signifies integer type and
# elements inside [] are the array elements
a2 = arr.array('d', [1.5, 2.4, 3.9])

# printing elements of array
print("Elements of the array" \
      "a2 is : ", end=" ")
for i in range(len(a2)):
    print(a2[i], end=", ")
print()

# Adding an item to the array

# Printing the elements of array a1
print("Original elements of the" \
      "array a1 is : ", end=" ")
print(*a1)

# Adding an element at the end of
# array by using the append method
a1.append(40)

# printing the modified array
print("Elements of the array a1" \
      "after adding an element" \
      "at last: ", end=" ")
print(*a1)

# Adding an element to the array at a
# specific index using the insert method
a1.insert(3, 35)

# printing the modified array
print("Elements of the array a1" \
      "after adding an element" \
      "at index 3: ", end=" ")
print(*a1)

# Removing an element from the array

# Removing an element by writing the elements itself
a1.remove(20)

# Printing the modified array
print("Array a1 after removing""element 20: ", end=" ")
print(*a1)

# Removing an element of a specific index
# Removing the element of array a1 present at index 2
a1.pop(2)

# Printing the modified array
print("Array a1 after removing""element of index 2: ", end=" ")
print(*a1)

# Python program to demonstrate
# that both list and array can
# be accessed sliced

# importing array module
import array as arr

# Declaring a list
List1 = [10, 20, 30, 20, 10, 40]

# Accessing a range of elements in the
# list using slicing operation

# Printing items of the list
# from index 1 to 3
print("List elements from ""index 1 to 4: ", List1[1:4])

# Printing items of the
# list from index 2 to end
print("List elements from " \
      "index 2 to last: ", List1[2:])

# Declaring an array
Array1 = arr.array('i',
                   [10, 20, 30, 40, 50, 60])

# Accessing a range of elements in the
# array using slicing operation
Sliced_array1 = Array1[1:4]
print("\nSlicing elements of the " \
      "array in a\nrange from index 1 to 4: ")
print(Sliced_array1)

# Print elements of the array
# from a defined point to end
Sliced_array2 = Array1[2:]
print("\nSlicing elements of the " \
      "array from\n2nd index till the end: ")
print(Sliced_array2)

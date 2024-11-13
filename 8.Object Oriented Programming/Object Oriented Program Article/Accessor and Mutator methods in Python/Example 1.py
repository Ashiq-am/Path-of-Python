# Python program to illustrate the use of
# Accessor and Mutator methods

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [5, 1, 3, 4, 2, 2, 7])

# Accesses the index of the value in argument
print(arr.index(2))

# Accesses the number of time the
# stated value is present
print(arr.count(2))

# Mutates the array list
(arr.append(19))

# Prints the array after alteration
print(arr)

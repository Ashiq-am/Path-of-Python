# Python program to demonstrate the
# difference between list and array in
# carrying out mathematical operations

# importing array module
from numpy import array

# declaring a list
List = [1, 2, 3]

# declaring an array
Array = array([1, 2, 3])

try:
    # adding 5 to each element of list
    List = List + 5

except(TypeError):
    print("Lists don't support list + int")

# for array
try:

    Array = Array + 5

    # printing the array
    print("Modified array: ", Array)

except(TypeError):
    print("Arrays don't support list + int")

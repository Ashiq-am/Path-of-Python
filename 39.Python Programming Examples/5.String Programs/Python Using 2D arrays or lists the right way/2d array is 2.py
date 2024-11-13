rows, cols = (5, 5)
# method 2b
arr = [[0 for i in range(cols)] for j in range(rows)]

# check if arr[0] and arr[1] refer to
# the same object
print(arr[0] is arr[1]) # prints False

# method 2a
arr = [[0]*cols]*rows

# check if arr[0] and arr[1] refer to
# the same object
# prints True because there is only one
# list object being created.
print(arr[0] is arr[1])

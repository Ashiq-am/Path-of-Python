# Python3 program to find modified array
# after executing m commands/queries

# Update function for every command
def updateQuery(arr, n, q, l, r, k):
    # If q == 0, add 'k' and '-k'
    # to 'l-1' and 'r' index
    if (q == 0):
        arr[l - 1] += k
        arr[r] += -k

    # If q == 1, add '-k' and 'k'
    # to 'l-1' and 'r' index
    else:
        arr[l - 1] += -k
        arr[r] += k

    return


# Function to generate the final
# array after executing all commands
def generateArray(arr, n):
    # Generate final array with the
    # help of DP concept
    for i in range(1, n):
        arr[i] += arr[i - 1]

    return


# Driver Code
n = 5
arr = [0 for i in range(n + 1)]

# Set all array elements to '0'
q = 0
l = 1
r = 3
k = 2
updateQuery(arr, n, q, l, r, k)

q, l, r, k = 1, 3, 5, 3
updateQuery(arr, n, q, l, r, k)

q, l, r, k = 0, 2, 5, 1
updateQuery(arr, n, q, l, r, k)

# Generate final array
generateArray(arr, n)

# Printing the final modified array
for i in range(n):
    print(arr[i], end=" ")

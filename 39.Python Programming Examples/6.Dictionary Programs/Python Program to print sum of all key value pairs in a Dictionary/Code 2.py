# Python3 implementation of the above approach

# Function to print the list
# containing the sum of key and
# value pairs from a dictionary
def FindSum(arr):
    # Stores the list containing the
    # sum of keys and values of each item
    l = []

    # Traverse the list of keys of arr
    for i in arr.keys():
        l.append(i + arr[i])

    # Print the list l
    print(*l)


# Driver Code

arr = {1: 10, 2: 20, 3: 30}

FindSum(arr)

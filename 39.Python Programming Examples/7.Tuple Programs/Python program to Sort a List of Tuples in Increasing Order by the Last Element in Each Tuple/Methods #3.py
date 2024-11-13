# Python program to sort a list of
# tuples by the second Item using sort()

# Function to sort hte list by second item of tuple
def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key=lambda x: x[-1])
    return tup


# Driver Code
tup = [(1, 3), (3, 2), (2, 1)]

# printing the sorted list of tuples
print(Sort_Tuple(tup))

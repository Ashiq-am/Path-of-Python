# Python3 program for the above approach

# Function to find the K-value
# for every index in the array
def print_h_index(arr, N):
    # Multiset to store the array
    # in the form of red-black tree
    ms = []

    # Iterating over the array
    for i in range(N):

        # Inserting the current
        # value in the multiset
        ms.append(arr[i])
        ms.sort()

        # Condition to check if
        # the smallest value
        # in the set is less than
        # it's size
        if (ms[0] < len(ms)):
            # Erase the smallest
            # value
            ms.pop(0)

        # h-index value will be
        # the size of the multiset
        print(len(ms), end=' ')


# Driver Code
if __name__ == '__main__':
    # Array
    arr = [9, 10, 7, 5, 0, 10, 2, 0]

    # Size of the array
    N = len(arr)

    # Function call
    print_h_index(arr, N)

# This code is contributed by pratham76

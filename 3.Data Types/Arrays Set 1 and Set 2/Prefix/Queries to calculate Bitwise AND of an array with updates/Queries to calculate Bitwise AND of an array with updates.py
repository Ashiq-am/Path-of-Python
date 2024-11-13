# Python3 program for the above approach

# Store the number of set bits at
# each position
prefixCount = [[0 for x in range(32)]
               for y in range(10000)]


# Function to precompute the prefix
# count array
def findPrefixCount(arr, size):
    # Iterate over the range[0, 31]
    for i in range(32):

        # Set the bit at position i
        # if arr[0] is set at position i
        prefixCount[i][0] = ((arr[0] >> i) & 1)

        # Traverse the array and
        # take prefix sum
        for j in range(1, size):
            # Update prefixCount[i][j]
            prefixCount[i][j] = ((arr[j] >> i) & 1)
            prefixCount[i][j] += prefixCount[i][j - 1]


# Function to find the Bitwise AND
# of all array elements
def arrayBitwiseAND(size):
    # Stores the required result
    result = 0

    # Iterate over the range [0, 31]
    for i in range(32):

        # Stores the number of set
        # bits at position i
        temp = prefixCount[i][size - 1]

        # If temp is N, then set ith
        # position in the result
        if (temp == size):
            result = (result | (1 << i))

    # Print the result
    print(result, end=" ")


# Function to update the prefix count
# array in each query
def applyQuery(currentVal, newVal, size):
    # Iterate through all the bits
    # of the current number
    for i in range(32):

        # Store the bit at position
        # i in the current value and
        # the new value
        bit1 = ((currentVal >> i) & 1)
        bit2 = ((newVal >> i) & 1)

        # If bit2 is set and bit1 is
        # unset, then increase the
        # set bits at position i by 1
        if (bit2 > 0 and bit1 == 0):
            prefixCount[i][size - 1] += 1

        # If bit1 is set and bit2 is
        # unset, then decrease the
        # set bits at position i by 1
        elif (bit1 > 0 and bit2 == 0):
            prefixCount[i][size - 1] -= 1


# Function to find the bitwise AND
# of the array after each query
def findbitwiseAND(queries, arr, N, M):
    # Fill the prefix count array
    findPrefixCount(arr, N)

    # Traverse the queries
    for i in range(M):
        # Store the index and
        # the new value
        id = queries[i][0]
        newVal = queries[i][1]

        # Store the current element
        # at the index
        currentVal = arr[id]

        # Update the array element
        arr[id] = newVal

        # Apply the changes to the
        # prefix count array
        applyQuery(currentVal, newVal, N)

        # Print the bitwise AND of
        # the modified array
        arrayBitwiseAND(N)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    queries = [[0, 2],
               [3, 3],
               [4, 2]]
    N = len(arr)
    M = len(queries)

    findbitwiseAND(queries, arr, N, M)

# This code is contributed by ukasp

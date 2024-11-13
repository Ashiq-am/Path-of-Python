# Python3 program for the above approach

# Function to count ways of spliting
# the array in two subarrays of equal
# sum by changing sign of any 1 element
def countSubArraySignChange(arr, N):
    # Stores the count of elements
    # in prefix and suffix of array
    prefixCount = {}
    suffixCount = {}

    # Stores the total sum of array
    total = 0

    # Traverse the array
    for i in range(N - 1, -1, -1):
        total += arr[i]

        # Increase the frequency of
        # current element in suffix
        suffixCount[arr[i]] = suffixCount.get(arr[i], 0) + 1

    # Stores prefix sum upto
    # an index
    prefixSum = 0

    # Stores sum of suffix
    # from an index
    suffixSum = 0

    # Stores the count of ways to
    # split the array in 2 subarrays
    # having equal sum
    count = 0

    # Traverse the array
    for i in range(N - 1):

        # Modify prefix sum
        prefixSum += arr[i]

        # Add arr[i] to prefix Map
        prefixCount[arr[i]] = prefixCount.get(arr[i], 0) + 1

        # Calculate suffix sum by
        # subtracting prefix sum
        # from total sum of elements
        suffixSum = total - prefixSum

        # Remove arr[i] from suffix Map
        suffixCount[arr[i]] -= 1

        # Store the difference
        # between the subarrays
        diff = prefixSum - suffixSum

        # Check if diff is even or not
        if (diff % 2 == 0):

            # Count number of ways to
            # split array at index i such
            # that subarray sums are same
            y, z = 0, 0
            if -diff // 2 in suffixCount:
                y = suffixCount[- diff// 2]
            if diff // 2 in prefixCount:
                z = prefixCount
            x = z + y

            # Update the count
            count = count + x

    # Return the count
    return count


# Driver Code
if __name__ == '__main__':
    arr = [2, 2, -3, 3]
    N = len(arr)

    # Function Call
    print(countSubArraySignChange(arr, N))

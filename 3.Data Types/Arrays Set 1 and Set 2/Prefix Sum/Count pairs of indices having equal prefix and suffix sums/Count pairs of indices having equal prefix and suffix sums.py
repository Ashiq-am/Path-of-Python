# Python3 program for the above approach

# Function to find the count of
# index pairs having equal
# prefix and suffix sums
def countPairs(arr, n):
    # Maps indices with prefix sums
    mp1 = {}
    sum = 0

    # Traverse the array
    for i in range(n):
        # Update prefix sum
        sum += arr[i]

        # Update frequency in Map
        mp1[sum] = mp1.get(sum, 0) + 1

    sum = 0
    ans = 0

    # Traverse the array in reverse
    for i in range(n - 1, -1, -1):

        # Update suffix sum
        sum += arr[i]

        # Check if any prefix sum of
        # equal value exists or not
        if (sum in mp1):
            ans += mp1[sum]

    # Print the obtained count
    print(ans)


# Driver code
if __name__ == '__main__':
    # Given array
    arr = [1, 2, 1, 1]

    # Given size
    n = len(arr)

    # Function Call
    countPairs(arr, n)

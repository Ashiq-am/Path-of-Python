# Python3 implementation to find array
# elements equal to the sum of any
# subarray of at least size 2

# Function to find all elements
def findElements(arr, n):
    if (n == 1):
        return

    pre = [0] * n

    # Create a prefix array
    pre[0] = arr[0]

    for i in range(1, n):
        pre[i] = arr[i] + pre[i - 1]

    mp = {}

    # Mark the sum of all sub arrays as true
    for i in range(1, n - 1):
        mp[pre[i]] = True

        for j in range(i + 1, n):
            mp[pre[j] - pre[i - 1]] = True

        # Check all elements which
    # are marked true in the map
    for i in range(n):
        if arr[i] in mp:
            print(arr[i], end=" ")
        else:
            pass

    print()


# Driver Code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    n1 = len(arr1)

    findElements(arr1, n1)

# Python3 program to implement
# the above approach

# For a given array arr,
# calculates the maximum j – i
# such that arr[j] > arr[i]

# Driver code
if __name__ == '__main__':

    v = [34, 8, 10, 3,
         2, 80, 30, 33, 1]
    n = len(v)
    maxFromEnd = [-38749432] * (n + 1)

    # Create an array maxfromEnd
    for i in range(n - 1, 0, -1):
        maxFromEnd[i] = max(maxFromEnd[i + 1],v[i])

    result = 0

    for i in range(0, n):
        low = i + 1
        high = n - 1
        ans = i

        while (low <= high):
            mid = int((low + high) / 2)

            if (v[i] <= maxFromEnd[mid]):

                # We store this as current
                # answer and look for further
                # larger number to the right side
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1

            # Keeping a track of the
        # maximum difference in indices
        result = max(result, ans - i)

    print(result, end="")


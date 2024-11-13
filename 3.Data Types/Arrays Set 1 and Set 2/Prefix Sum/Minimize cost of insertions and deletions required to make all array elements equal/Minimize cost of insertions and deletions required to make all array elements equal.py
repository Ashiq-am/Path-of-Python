# Python program to implement
# the above approach

# Function to find minimum cost required
# to make all array elements equal
def minCost(arr, A, B, N):
    # Sort the array
    arr.sort()

    # Stores the prefix sum and sum
    # of the array respectively
    cumarr = [0] * N
    sum = 0

    # Traverse the array
    for i in range(N):
        # Update sum
        sum += arr[i]

        # Update prefix sum
        cumarr[i] = sum

    # Update middle element
    mid = (N - 1) // 2

    # Calculate cost to convert
    # every element to mid element
    ans = (arr[mid] * (mid + 1) - cumarr[mid]) * A \
          + (cumarr[N - 1] - cumarr[mid] - (arr[mid] * (N - 1 - mid))) * B
    if (A == B):
        return ans
    elif (A < B):
        low = mid
        high = N - 1

        # Binary search
        while (low <= high):
            mid = low + (high - low) // 2
            curr = (arr[mid] * (mid + 1) - cumarr[mid]) * A \
                   + (cumarr[N - 1] - cumarr[mid] - (arr[mid] * (N - 1 - mid))) * B
            if (curr <= ans):
                ans = curr
                low = mid + 1
            else:
                high = mid - 1
        return ans
    else:
        low = 0
        high = mid

        # Binary search
        while (low <= high):
            mid = low + (high - low) // 2
            curr = (arr[mid] * (mid + 1) - cumarr[mid]) * A \
                   + (cumarr[N - 1] - cumarr[mid] - (arr[mid] * (N - 1 - mid))) * B
            if (curr <= ans):
                ans = curr
                high = mid - 1
            else:
                low = mid + 1
        return ans


# Driver Code
if __name__ == '__main__':
    arr = [2, 5, 6, 9, 10, 12, 15]
    A = 1
    B = 2
    N = (int)(len(arr))

    print(minCost(arr, A, B, N))



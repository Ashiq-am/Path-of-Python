# python3 code to implement the approach

INT_MAX = +2147483647
INT_MIN = -2147483648

# Function to calculate the sum of elements


def MaximumValue(n, q, arr, queries):

    arr.sort()

    prefixArr = [0 for _ in range(n + 1)]
    ans = [0 for _ in range(q)]

    for i in range(0, n):
        prefixArr[i + 1] = prefixArr[i] + arr[i][1]

    # Binary search for start
    for i in range(0, q):
        start = INT_MAX
        end = INT_MIN
        l = 0
        h = n - 1
        while (l <= h):
            mid = l + (h - l) // 2
            if (arr[mid][0] >= queries[i][0]):
                start = min(start, mid)
                h = mid - 1

            else:
                l = mid + 1

        # Binary search for end
        l = 0
        h = n - 1
        while (l <= h):
            mid = l + (h - l) // 2
            if (arr[mid][0] <= queries[i][1]):
                end = max(end, mid)
                l = mid + 1

            else:
                h = mid - 1

        if (end + 1 < 0 or start >= len(prefixArr)):
            ans[i] = 0

        else:
            ans[i] = prefixArr[end + 1] - prefixArr[start]

    # Return the answers for all the queries
    return ans


# Driver code
if __name__ == "__main__":
    N = 5
    Q = 3
    arr = [
        [1, 2], [3, 2], [4, 5], [7, 1], [10, 4]
    ]
    queries = [[0, 12], [4, 6], [2, 8]]

    # Function call
    ans = MaximumValue(N, Q, arr, queries)
    for x in ans:
        print(x, end=" ")

    # This code is contributed by rakeshsahni
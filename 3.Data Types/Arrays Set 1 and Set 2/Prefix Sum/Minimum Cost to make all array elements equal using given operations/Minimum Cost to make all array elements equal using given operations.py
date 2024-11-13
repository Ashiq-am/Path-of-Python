# Python3 implementation to find the
# minimum cost to make all array
# elements equal
def lowerBound(array, length, value):
    low = 0
    high = length

    while (low < high):
        mid = (low + high) // 2

        # Checks if the value is less
        # than middle element of the array
        if (value <= array[mid]):
            high = mid
        else:
            low = mid + 1

    return low


# Function that returns the cost of makeing
# all elements equal to current element
def costCalculation(current, arr,n, pref, a, r, minimum):
    # Compute the lower bound
    # of current element
    index = lowerBound(arr, len(arr), current)

    # Calculate the requirement
    # of add operation
    left = index * current - pref[index]

    # Calcuate the requirement
    # of subtract operation
    right = (pref[n] - pref[index] - (n - index) * current)

    # Compute minimum of left and right
    res = min(left, right)
    left -= res
    right -= res

    # Computing the total cost of add
    # and subtract operations
    total = res * minimum
    total += left * a
    total += right * r

    return total


# Function that prints minimum cost
# of making all elements equal
def solve(arr, n, a, r, m):
    # Sort the given array
    arr.sort()

    # Calcuate minimum from a + r and m
    minimum = min(a + r, m)

    pref = [0] * (n + 1)

    # Compute prefix sum and
    # store in pref array
    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]

    ans = 10000

    # Find the minimum cost
    # from the given elements
    for i in range(n):
        ans = min(ans, costCalculation(arr[i], arr,n, pref, a,r, minimum))

    # Finding the minimum cost
    # from the other cases where
    # minimum cost can occur
    ans = min(ans, costCalculation(pref[n] // n,arr, n, pref,a, r, minimum))
    ans = min(ans, costCalculation(pref[n] // n + 1,arr, n, pref, a, r, minimum))

    # Printing the minimum cost of making
    # all elements equal
    print(ans)


# Driver Code
if __name__ == "__main__":
    arr = [5, 5, 3, 6, 5]
    A = 1
    R = 2
    M = 4
    size = len(arr)

    # Function call
    solve(arr, size, A, R, M)

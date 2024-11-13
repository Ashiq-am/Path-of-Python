# Python3 program for the above approach

# Function to check if difference
# between the sum of odd and even
# indexed elements after removing
# the first element is K or not
def findCount0th(arr, N, K):
    # Stores the sum of elements
    # at odd and even indices
    oddsum = 0
    evensum = 0

    for i in range(1, N, 2):
        oddsum += arr[i]

    for i in range(2, N, 2):
        evensum += arr[i]

    # Return 1 if difference is K
    if (abs(oddsum - evensum) == K):
        return 1
    else:
        return 0


# Function to check if difference
# between the sum of odd and even
# indexed elements after removing
# the second element is K or not
def findCount1st(arr, N, K):
    # Stores the sum of elements
    # at odd and even indices
    evensum = arr[0]
    oddsum = 0

    for i in range(3, N, 2):
        evensum += arr[i]

    for i in range(2, N, 2):
        oddsum += arr[i]

    # Return 1 if difference is K
    if (abs(oddsum - evensum) == K):
        return 1
    else:
        return 0


# Function to count number of elements
# to be removed to make sum of
# differences between odd and even
# indexed elements equal to K
def countTimes(arr, K):
    # Size of given array
    N = len(arr)

    # Base Conditions
    if (N == 1):
        return 1

    if (N < 3):
        return 0

    if (N == 3):
        cnt = 0

        if abs(arr[0] - arr[1]) == K:
            cnt += 1

        if abs(arr[2] - arr[1]) == K:
            cnt += 1

        if abs(arr[0] - arr[2]) == K:
            cnt += 1

        return cnt

    # Stores prefix and suffix sums
    prefix = [0] * (N + 2)
    suffix = [0] * (N + 2)

    # Base assignments
    prefix[0] = arr[0]
    prefix[1] = arr[1]
    suffix[N - 1] = arr[N - 1]
    suffix[N - 2] = arr[N - 2]

    # Store prefix sums of even
    # indexed elements
    for i in range(2, N, 2):
        prefix[i] = arr[i] + prefix[i - 2]

    # Store prefix sums of odd
    # indexed elements
    for i in range(3, N, 2):
        prefix[i] = arr[i] + prefix[i - 2]

    # Similarly, store suffix sums of
    # elements at even and odd indices
    for i in range(N - 3, -1, -2):
        suffix[i] = arr[i] + suffix[i + 2]

    for i in range(N - 4, -1, -2):
        suffix[i] = arr[i] + suffix[i + 2]

    # Stores the count of possible removals
    count = 0

    # Traverse and remove the ith element
    for i in range(2, N):

        # If the current element is
        # excluded, then previous index
        # (i - 1) points to (i + 2)
        # and (i - 2) points to (i + 1)
        if (abs(prefix[i - 1] + suffix[i + 2] -
                prefix[i - 2] - suffix[i + 1]) == K):
            count += 1

    # Find count when 0th element is removed
    count += findCount0th(arr, N, K)

    # Find count when 1st element is removed
    count += findCount1st(arr, N, K)

    # Count gives the required answer
    return count


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    K = 2

    # Function call
    print(countTimes(arr, K))

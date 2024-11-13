# Python3 program for the above approach

# Function to find the
# largest size subarray
def func(arr, k, n):
    # Variable declaration
    ans = n
    Sum = 0
    start = 0

    # Loop till N
    for end in range(n):

        # Sliding window from left
        Sum += arr[end]

        while (Sum > k):

            # Sliding window from right
            Sum -= arr[start]
            start += 1

            # Storing sub-array size - 1
            # for which sum was greater than k
            ans = min(ans, end - start + 1)

            # Sum will be 0 if start>end
            # because all elements are positive
            # start>end only when arr[end]>k i.e,
            # there is an array element with
            # value greater than k, so sub-array
            # sum cannot be less than k.
            if (Sum == 0):
                break

        if (Sum == 0):
            ans = -1
            break

    # Print the answer
    print(ans)


# Driver code
arr = [1, 2, 3, 4]
k = 8
n = len(arr)

# Function call
func(arr, k, n)

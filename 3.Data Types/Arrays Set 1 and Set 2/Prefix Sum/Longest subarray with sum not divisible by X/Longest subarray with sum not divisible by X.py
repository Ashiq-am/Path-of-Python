# Python3 program to implement
# the above approach

# Function to print the longest
# subarray with sum of elements
# not divisible by X
def max_length(N, x, v):
    # Pref[] stores the prefix sum
    # Suff[] stores the suffix sum
    preff, suff = [], []
    ct = 0

    for i in range(N):
        a = v[i]

        # If array element is
        # divisibile by x
        if a % x == 0:
            # Increase count
            ct += 1

    # If all the array elements
    # are divisible by x
    if ct == N:
        # No subarray possible
        print(-1)
        return

    # Reverse v to calculate the
    # suffix sum
    v.reverse()

    suff.append(v[0])

    # Calculate the suffix sum
    for i in range(1, N):
        suff.append(v[i] + suff[i - 1])

    # Reverse to original form
    v.reverse()

    # Reverse the suffix sum array
    suff.reverse()

    preff.append(v[0])

    # Calculate the prefix sum
    for i in range(1, N):
        preff.append(v[i] + preff[i - 1])

    ans = 0

    # Stores the starting index
    # of required subarray
    lp = 0

    # Stores the ending index
    # of required subarray
    rp = N - 1

    for i in range(N):

        # If suffix sum till i-th
        # index is not divisible by x
        if suff[i] % x != 0 and ans < N - 1:
            lp = i
            rp = N - 1

            # Update the answer
            ans = max(ans, N - i)

        # If prefix sum till i-th
        # index is not divisible by x
        if preff[i] % x != 0 and ans < i + 1:
            lp = 0
            rp = i

            # Update the answer
            ans = max(ans, i + 1)

        # Print the longest subarray
    for i in range(lp, rp + 1):
        print(v[i], end=" ")

    # Driver code


x = 3
v = [1, 3, 2, 6]
N = len(v)

max_length(N, x, v)



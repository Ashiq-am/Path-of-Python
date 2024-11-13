# Python3 implementation to find the
# minimum size subarray containing
# all unique elements after processing
# the array for K queries of ranges

# Function to find minimum size subarray
# of all array elements
def subarrayLength(A, R, N, M):
    # Updating the array after
    # processing each query
    for i in range(M):

        l = R[i][0]
        r = R[i][1] + 1

        # Making it to 0-indexing
        l -= 1
        r -= 1

        # Prefix sum array concept is used
        # to obtain the count array
        A[l] += 1

        if (r < N):
            A[r] -= 1

    # Iterating over the array
    # to get the final array
    for i in range(1, N):
        A[i] += A[i - 1]

    # Variable to get count
    # of all unique elements
    count = 0

    # Hash to maintain perviously
    # occured elements
    s = []

    # Loop to find the all
    # unique elements
    for i in range(N):
        if (A[i] not in s):
            count += 1

        s.append(A[i])

    # Array to maintain counter
    # of encountered elements
    repeat = [0] * (count + 1)

    # Variable to store answer
    ans = N

    # Using two pointers approach
    counter, left, right = 0, 0, 0

    while (right < N):

        cur_element = A[right]
        repeat[cur_element] += 1

        # Increment counter
        # if occured once
        if (repeat[cur_element] == 1):
            counter += 1

        # When all unique
        # elements are found
        while (counter == count):

            # update answer with
            # minimum size
            ans = min(ans, right - left + 1)

            # Decrement count of
            # elements from left
            cur_element = A[left]
            repeat[cur_element] -= 1
            left += 1

            # Decrement counter
            if (repeat[cur_element] == 0):
                counter -= 1

        right += 1

    return ans


# Driver code
if __name__ == "__main__":
    N, queries = 8, 6
    Q = [[1, 4], [3, 4], [4, 5],
         [5, 5], [7, 8], [8, 8]]

    A = [0] * N
    print(subarrayLength(A, Q, N, queries))

# Python3 program to implement
# the above approach

# Function to find the
# maximum product possible
def maxValue(a, n):
    # Stores prefix sum
    presum = [0 for i in range(n)]

    presum[0] = a[0]

    # Find the prefix sum array
    for i in range(1, n, 1):
        presum[i] = presum[i - 1] + a[i]

    # l[] and r[] stores index of
    # nearest smaller elements on
    # left and right respectively
    l = [0 for i in range(n)]
    r = [0 for i in range(n)]

    st = []

    # Find all left index
    for i in range(1, n):

        # Until stack is non-empty
        # & top element is greater
        # than the current element
        while (len(st) and
               a[st[len(st) - 1]] >= a[i]):
            st.remove(st[len(st) - 1])

        # If stack is empty
        if (len(st)):
            l[i] = st[len(st) - 1] + 1;
        else:
            l[i] = 0

        # Push the current index i
        st.append(i)

    # Reset stack
    while (len(st)):
        st.remove(st[len(st) - 1])

    # Find all right index
    i = n - 1
    while (i >= 0):

        # Until stack is non-empty
        # & top element is greater
        # than the current element
        while (len(st) and
               a[st[len(st) - 1]] >= a[i]):
            st.remove(st[len(st) - 1])

            if (len(st)):
                r[i] = st[len(st) - 1] - 1
            else:
                r[i] = n - 1

        # Push the current index i
        st.append(i)
        i -= 1

    # Stores the maximum product
    maxProduct = 0

    # Iterate over the range [0, n)
    for i in range(n):

        # Calculate the product
        if l[i] == 0:
            tempProduct = (a[i] *
                           presum[r[i]])
        else:
            tempProduct = (a[i] *
                           (presum[r[i]] -
                            presum[l[i] - 1]))

        # Update the maximum product
        maxProduct = max(maxProduct,
                         tempProduct)

    # Return the maximum product
    print(maxProduct)


# Driver Code
if __name__ == '__main__':
    # Given array
    n = 6
    arr = [3, 1, 6, 4, 5, 2]

    # Function call
    maxValue(arr, n)

# python code for the above approach
# // Function to find minimum operations
# // needed to make the product of any
# // two adjacent elements in prefix
# // sum array negative
def minOperations(a):
    # Stores the minimum operations
    res = 100000000000
    N = len(a)
    for r in range(0, 2):

        # Stores the prefix sum
        # and number of operations
        sum = 0
        ans = 0

        # Traverse the array
        for i in range(0, N):

            # Update the value of sum
            sum += a[i]

            # Check if i+r is odd
            if ((i + r) % 2):

                # Check if prefix sum
                # is not positive
                if (sum <= 0):
                    # Update the value of
                    # ans and sum
                    ans += -sum + 1
                    sum = 1
            else:

                # Check if prefix sum is
                # not negative
                if (sum >= 0):
                    # Update the value of
                    # ans and sum
                    ans += sum + 1
                    sum = -1

        # Update the value of res
        res = min(res, ans)

    # // Print the value of res
    print(res)


# Driver code
a = [1, -3, 1, 0]
minOperations(a)



# Python 3 program to find maximum array
# sum with multiplications of a prefix
# and a suffix with -1 allowed.

# function to maximize the sum
def maximize(a, n):
    # stores the pre sum
    presum = [0] * n

    # to store sum from 0 to i
    sm = 0

    # stores the maximum sum with
    # prefix multiplication with -1.
    max_sum = 0

    # traverse from 0 to n
    for i in range(0, n):
        # calculate the presum
        presum[i] = max_sum

        # calculate sum
        max_sum = max_sum + a[i]
        sm = sm + a[i]

        max_sum = max(max_sum, -sm)

    # Initialize answer.
    ans = max(sm, max_sum)

    # traverse from back to start
    g = 0
    for i in range(n - 1, -1, -1):
        # stores the sum multiplied by (-1)
        g = g - a[i]

        # stores the max of ans and
        # presum + (-1*negative sum);
        ans = max(ans, g + presum[i])

    # returns answer
    return ans


# driver program to test the above function
a = [-4, 2, 0, 5, 0]
n = len(a)
print(maximize(a, n))

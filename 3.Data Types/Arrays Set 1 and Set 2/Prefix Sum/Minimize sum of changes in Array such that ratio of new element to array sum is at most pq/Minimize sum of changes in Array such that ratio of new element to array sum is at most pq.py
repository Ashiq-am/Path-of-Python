# Python code for the above approach
import sys


# function to check if the candidate sum
# satisfies the condition of the problem
def isValid(candidate, pre, n, A, p, q):
    # flag variable to check wrong answer
    flag = True
    for i in range(1, n):

        # Now for each element, we are checking
        # if its ratio with sum of all previous
        # elements + candidate is greater than p/q.
        # If so, we will return false.
        curr_sum = pre[i - 1] + candidate
        if (A[i] * q > p * curr_sum):
            flag = False
            break

    # comparing like A[i]/(curr_sum)>p/q
    # will be error prone.

    return flag


def solve(n, A, p, q):
    # declaring and constructing
    # prefix sum array
    pre = [0] * 100
    pre[0] = A[0]
    for i in range(1, n):
        pre[i] = A[i] + pre[i - 1]

    # setting lower and upper bound for
    # binary search
    lo = 0
    hi = sys.maxsize
    ans = sys.maxsize

    # since minimum answer is needed,
    # so it is initialized with INT_MAX
    while (lo <= hi):

        # calculating mid by using (lo+hi)/2
        # may overflow in certain cases
        mid = lo + (hi - lo) // 2

        # checking if required ratio would be
        # achieved by all elements if "mid" is
        # considered as answer
        if (isValid(mid, pre, n, A, p, q)):
            ans = mid
            hi = mid - 1

        else:
            lo = mid + 1

    return ans


# Driver Function
n = 4
p = 1
q = 100
A = [20100, 1, 202, 202]

# printing the required answer
print(solve(n, A, p, q))

# This code is contributed by code_hunt.

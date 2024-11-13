# Python3 program to count number of
# substring under given condition
import math


# Function return count of such
# substing
def countOfSubstrings(s):
    n = len(s)

    # Selection of adequate x value
    x = int(math.sqrt(n))

    # Store where 1's are located
    ones = []

    for i in range(n):
        if (s[i] == '1'):
            ones.append(i)

        # If there are no ones,
    # then answer is 0
    if (len(ones) == 0):
        return 0

    # For ease of implementation
    ones.append(n)

    # Count storage
    totCount = [0] * (n * x + n)

    sum = 0

    # Iterate on all k values less
    # than fixed x
    for k in range(x + 1):

        # Keeps a count of 1's occured
        # during string traversal
        now = 0
        totCount[k * n] += 1

        # Iterate on string and modify
        # the totCount
        for j in range(1, n + 1):

            # If this character is 1
            if (s[j - 1] == '1'):
                now += 1
            index = j - k * now

            # Add to the final sum/count
            sum += totCount[index + k * n]

            # Increase totCount at exterior
            # position
            totCount[index + k * n] += 1

        now = 0
        totCount[k * n] -= 1

        for j in range(1, n + 1):
            if (s[j - 1] == '1'):
                now += 1
            index = j - k * now

            # Reduce totCount at index + k*n
            totCount[index + k * n] -= 1

    # Slightly modified prefix sum storage
    prefix_sum = [-1] * n

    # Number of 1's till i-1
    cnt = 0

    for i in range(n):
        prefix_sum[i] = cnt
        if (s[i] == '1'):
            cnt += 1

    # Traversing over string considering
    # each position and finding bounds
    # and count using the inequalities
    for k in range(n):
        j = 1
        while (j <= (n // x) and
               prefix_sum[k] + j <= cnt):

            # Calculating bounds for l and r
            l = (ones[prefix_sum[k] + j - 1] -
                 k + 1)

            r = ones[prefix_sum[k] + j] - k
            l = max(l, j * (x + 1))

            # If valid then add to answer
            if (l <= r):
                sum += r // j - (l - 1) // j

            j += 1

    return sum


# Driver code
if __name__ == "__main__":
    S = "1111100000"

    print(countOfSubstrings(S))

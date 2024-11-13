# Python3 program for the above approach
from math import log


# Function to implement fast
# exponentiation
def binpow(a, b):
    res = 1
    while (b > 0):
        if (b % 2 == 1):
            res = res * a
        a = a * a
        b //= 2
    return res


# Function to return the value
# for powers of 2
def find(x):
    if (x == 0):
        return 0
    p = log(x) / log(2)
    return binpow(2, p + 1) - 1


# Function to convert N into binary
def getBinary(n):
    # To store binary representation
    ans = ""

    # Iterate each digit of n
    while (n > 0):
        dig = n % 2
        ans += str(dig)
        n //= 2

    # Return binary representation
    return ans


# Function to find difference in bits
def totalCountDifference(n):
    # Get binary representation
    ans = getBinary(n)

    # total number of bit
    # differences from 0 to N
    req = 0

    # Iterate over each binary bit
    for i in range(len(ans)):

        # If current bit is '1' then add
        # the count of current bit
        if (ans[i] == '1'):
            req += find(binpow(2, i))
    return req


# Driver Code

# Given Number
N = 5

# Function Call
print(totalCountDifference(N))

# This code is contributed by shubhamsingh10

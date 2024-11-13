# Python 3 program to find the divisor of all
# except for exactly one element in an array.
from math import gcd


# Function to find the divisor of all
# except for exactly one element in an array.
def getDivisor(a, n):
    # There's only one element in the array
    if (n == 1):
        return (a[0] + 1)

    P = [0] * n
    S = [0] * n

    # Creating prefix array of GCD
    P[0] = a[0]
    for i in range(1, n):
        P[i] = gcd(a[i], P[i - 1])

    # Creating suffix array of GCD
    S[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        S[i] = gcd(S[i + 1], a[i])

    # Iterate through the array
    for i in range(0, n + 1):

        # Variable to store the divisor
        cur = 0

        # Getting the divisor
        if (i == 0):
            cur = S[i + 1]
        elif (i == n - 1):
            cur = P[i - 1]
        else:
            cur = gcd(P[i - 1], S[i + 1])

        # Check if it is not a divisor of a[i]
        if (a[i] % cur != 0):
            return cur

    return 0;


# Driver Code
if __name__ == '__main__':
    a = [12, 6, 18, 12, 16]
    n = len(a)

    print(getDivisor(a, n))

# This code is contributed by Rupesh Rao

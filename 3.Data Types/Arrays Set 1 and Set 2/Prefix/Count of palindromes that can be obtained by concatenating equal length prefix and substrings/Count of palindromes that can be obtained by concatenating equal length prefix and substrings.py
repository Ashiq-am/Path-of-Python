# Python3 program the above approach

# Function to calculate the
# number of palindromes
def countPalindrome(S):
    N = len(S)
    Z = [0] * N

    # Calculation of Z-array
    l = 0
    r = 0
    for i in range(1, N):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - 1])
        while ((i + Z[i]) < N and (S[Z[i]] == S[i + Z[i]])):
            Z[i] += 1
        if ((i + Z[i] - 1) > r):
            l = ir = i + Z[i] - 1

    # Calculation of sigma(Z[i]+1)
    sum = 0
    for i in range(0, len(Z)):
        sum += Z[i] + 1

    # return the count
    return sum


# Driver code

# Given String
S = "abab"
print(countPalindrome(S))

# This code is contributed by virusbuddah

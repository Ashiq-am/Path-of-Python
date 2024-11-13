# Python3 program to implement
# the above approach

# Function to check whether the
# substring from l to r is
# palindrome or not
def isPalindrome(l, r, s):
    while (l <= r):

        # If characters at l and
        # r differ
        if (s[l] != s[r]):
            # Not a palindrome
            return bool(False)

        l += 1
        r -= 1

    # If the string is
    # a palindrome
    return bool(True)


# Function to count and return
# the number of possible splits
def numWays(s):
    n = len(s)

    # Stores the count
    # of splits
    ans = 0
    for i in range(n - 1):

        # Check if the two substrings
        # after the split are
        # palindromic or not
        if (isPalindrome(0, i, s) and
                isPalindrome(i + 1, n - 1, s)):
            # If both are palindromes
            ans += 1

    # Print the final count
    return ans


# Driver Code
S = "aaaaa"

print(numWays(S))

# This code is contributed by divyeshrabadiya07

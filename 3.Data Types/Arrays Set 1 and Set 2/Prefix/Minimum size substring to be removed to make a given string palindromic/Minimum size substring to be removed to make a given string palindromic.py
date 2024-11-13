# Python3 program of the
# above approach

# Function to find palindromic
# prefix of maximum length
def palindromePrefix(S):
    n = len(S)

    # Finding palindromic prefix
    # of maximum length
    for i in range(n - 1, -1, -1):
        curr = S[0: i + 1]

        # Checking if curr substring
        # is palindrome or not.
        l = 0
        r = len(curr) - 1
        is_palindrome = 1

        while (l < r):
            if (curr[l] != curr[r]):
                is_palindrome = 0
                break

            l += 1
            r -= 1

        # Condition to check if the
        # prefix is a palindrome
        if (is_palindrome):
            return curr

    # if no palindrome exist
    return ""


# Function to find the maximum
# size palindrome such that
# after removing minimum size
# substring
def maxPalindrome(S):
    n = len(S)
    if (n <= 1):
        return S

    pre = ""
    suff = ""

    # Finding prefix and
    # suffix of same length
    i = 0
    j = n - 1
    while (S[i] == S[j] and
           i < j):
        i += 1
        j -= 1

    # Matching the ranges
    i -= 1
    j += 1

    pre = S[0: i + 1]
    suff = S[j:]

    # It is possible that the
    # whole string is palindrome.

    # Case 1: Length is even and
    # whole string is palindrome
    if (j - i == 1):
        return pre + suff

    # Case 2: Length is odd and
    # whole string is palindrome
    if (j - i == 2):
        # Adding that mid character
        mid_char = S[i + 1: i + 2]

        return pre + mid_char + suff

    # Add prefix or suffix of the
    # remaining string or suffix,
    # whichever is longer
    rem_str = S[i + 1: j]

    pre_of_rem_str = palindromePrefix(rem_str)

    # Reverse the remaining string to
    # find the palindromic suffix
    list1 = list(rem_str)

    list1.reverse()
    rem_str = ''.join(list1)
    suff_of_rem_str = palindromePrefix(rem_str)

    if (len(pre_of_rem_str) >=
            len(suff_of_rem_str)):
        return (pre + pre_of_rem_str +
                suff)
    else:
        return (pre + suff_of_rem_str +
                suff)


# Driver Code
if __name__ == "__main__":
    S = "geeksforskeeg"
    print(maxPalindrome(S))

# This code is contributed by Chitranayal

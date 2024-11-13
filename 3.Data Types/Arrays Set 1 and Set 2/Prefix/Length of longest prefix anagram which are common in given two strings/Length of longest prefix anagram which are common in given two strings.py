# Python3 program for the above approach
SIZE = 26


# Function to check if two arrays
# are identical or not
def longHelper(freq1, freq2):
    # Iterate over the range [0, SIZE]
    for i in range(26):

        # If frequency any character is
        # not same in both the strings
        if (freq1[i] != freq2[i]):
            return False

    # Otherwise
    return True


# Function to find the maximum
# length of the required string
def longCommomPrefixAnagram(s1, s2, n1, n2):
    # Store the count of
    # characters in str1
    freq1 = [0] * 26

    # Store the count of
    # characters in str2
    freq2 = [0] * 26

    # Stores the maximum length
    ans = 0

    # Minimum length of str1 and str2
    mini_len = min(n1, n2)
    for i in range(mini_len):

        # Increment the count of
        # characters of str1[i] in
        # freq1[] by one
        freq1[ord(s1[i]) - ord('a')] += 1

        # Increment the count of
        # characters of stord(r2[i]) in
        # freq2[] by one
        freq2[ord(s2[i]) - ord('a')] += 1

        # Checks if prefixes are
        # anagram or not
        if (longHelper(freq1, freq2)):
            ans = i + 1

    # Finally print the ans
    print(ans)


# Driver Code
if __name__ == '__main__':
    str1 = "abaabcdezzwer"
    str2 = "caaabbttyh"
    N = len(str1)
    M = len(str2)

    # Function Call
    longCommomPrefixAnagram(str1, str2, N, M)

# This code is contributed by mohit kumar 29.

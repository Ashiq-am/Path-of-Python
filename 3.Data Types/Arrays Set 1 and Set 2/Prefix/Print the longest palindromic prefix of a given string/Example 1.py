# Python3 program for the above approach

# Function to find the longest prefix
# which is palindrome
def LongestPalindromicPrefix(string):
    # Find the length of the given string
    n = len(string)

    # For storing the length of longest
    # Prefix Palindrome
    max_len = 0

    # Loop to check the substring of all
    # length from 1 to n which is palindrome
    for length in range(0, n + 1):

        # String of length i
        temp = string[0:length]

        # To store the value of temp
        temp2 = temp

        # Reversing the value of temp
        temp3 = temp2[::-1]

        # If string temp is palindromic
        # then update the length
        if temp == temp3:
            max_len = length

    # Print the palindromic string
    # of max_len
    print(string[0:max_len])


# Driver code
if __name__ == '__main__':
    string = "abaac";

    # Function call
    LongestPalindromicPrefix(string)

# This code is contributed by virusbuddah_

# Python3 program to find the number of occurrences
# of a character at position P upto p-1

# Function to find the number of occurrences
# of a character at position P upto p-1
def countOccurrence(s, position):
    alpha = [0] * 26
    b = [0] * len(s)

    # Iterate over the string
    for i in range(0, len(s)):
        # Store the Occurrence of same character
        b[i] = alpha[ord(s[i]) - 97]

        # Increase its frequency
        alpha[ord(s[i]) - 97] = alpha[ord(s[i]) - 97] + 1

    # Return the required count
    return b[position - 1]


# Driver code
s = "ababababab"

p = 9

# Function call
print(countOccurrence(s, p))

# This code is contributed by Sanjit_Prasad

# Python code for the above approach

# Function to return a string
# found from the coded string
def findstring(str):
    # Declaring string to store result
    result = ""

    # Loop to generate the original string
    for i in range(len(str)):

        # If current character in string
        # is '*' add result to itself
        if (str[i] == '*'):
            result += result

        # Else add current element only
        else:
            result += str[i]
    # Return the result
    return result


# Driver code
str = "ab*c*d"
print(findstring(str))

# This code is contributed by Saurabh Jaiswal

# Python code to implement the above approach

# Function to find the largest substring
def findLargest(s):

    maxi = -1
    sum = 0

    # Loop to find the largest substring
    # satisfying the given conditions
    for i in range(1, len(s) - 1):
        if (s[i] != s[0] and s[i] != s[len(s) - 1]):
            sum += 1

        else:
            maxi = max(sum, maxi)
            sum = 0


    maxi = max(sum, maxi)
    if (maxi == 0):
        maxi = -1

    # Return the maximum length
    return maxi

# Driver code
if __name__ == "__main__":

    s = "abcdefb"

    # Function call
    print(findLargest(s))

# This code is contributed by hrithikgarg03188.

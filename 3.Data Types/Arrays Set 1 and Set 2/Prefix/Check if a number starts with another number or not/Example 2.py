# Python3 program for the
# above approach

# Function to check if B is
# a prefix of A or not
def checkprefix(A, B):
    # Convert numbers into strings
    s1 = str(A)
    s2 = str(B)

    # Check if s2 is a prefix of s1
    # or not using startswith() function
    result = s1.startswith(s2)

    # If result is true print Yes
    if result:
        print("Yes")
    else:
        print("No")


# Driver code
if __name__ == '__main__':
    # Given numbers
    A = 12345
    B = 12

    # Function call
    checkprefix(A, B)

# This code is contributed by virusbuddah_

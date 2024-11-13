# Python3 program for the
# above approach

# Function to check if B is
# a prefix of A or not
def checkprefix(A, B):
    # Convert numbers into strings
    s1 = str(A)
    s2 = str(B)

    # Find the length of s1 and s2
    n1 = len(s1)
    n2 = len(s2)

    # Base case
    if n1 < n2:
        return False

    # Traverse the string s1 and s2
    for i in range(0, n2):

        # If at any index characters
        # are unequal then return False
        if s1[i] != s2[i]:
            return False

    return True


# Driver code
if __name__ == '__main__':

    # Given numbers
    A = 12345
    B = 12

    # Function call
    result = checkprefix(A, B)

    # If B is a prefix of A ,
    # then print Yes
    if result:
        print("Yes")
    else:
        print("No")

# This code is contributed by virusbuddah_

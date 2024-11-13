# Python program for the above approach

# Function to count flips required
# to make strings A and B equal
def findOperations(A, B, N):
    # Stores the count of the
    # number of operations
    operations = 0

    # Stores the length of
    # the chosen prefixes
    ops = []

    # Stores if operations are
    # performed even or odd times
    invert = False

    # Traverse the given string
    for i in range(N - 1, -1, -1):

        # If current characters in
        # the two strings are unequal
        if (A[i] != B[i]):

            # If A[i] is not flipped
            if (not invert):
                # Increment count
                # of operations
                operations += 1

                # Insert the length of
                # the chosen prefix
                ops.append(i + 1)

                # Update invert to true
                invert = True
        else:

            # If A[i] is flipped
            if (invert):
                # Increment count
                # of operations
                operations += 1

                # Insert length of
                # the chosen prefix
                ops.append(i + 1)

                # Update invert to false
                invert = False

    # Print the number of
    # operations required
    print(operations)

    # Print the chosen prefix
    # length in each operation
    if (operations != 0):
        for x in ops:
            print(x, end=" ")


# Driver Code
if __name__ == '__main__':
    # Given binary strings
    A, B = "001", "000"
    N = len(A)

    findOperations(A, B, N)

# This code is contributed by mohit kumar 29.

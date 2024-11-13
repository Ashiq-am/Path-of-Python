# Python 3 program for the above approach
import sys


# Function that counts minimum
# character that must be removed
def min_remove(st):
    # Length of string
    N = len(st)

    # Create prefix array
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    prefix_c = [0] * (N + 1)

    # Initialize first position
    prefix_a[0] = 0
    prefix_b[0] = 0
    prefix_c[0] = 0

    # Fill prefix array
    for i in range(1, N + 1):

        if (st[i - 1] == 'a'):
            prefix_a[i] = (prefix_a[i - 1] + 1)
        else:
            prefix_a[i] = prefix_a[i - 1]

        if (st[i - 1] == 'b'):
            prefix_b[i] = (prefix_b[i - 1] + 1)
        else:
            prefix_b[i] = prefix_b[i - 1]

        if (st[i - 1] == 'c'):
            prefix_c[i] = (prefix_c[i - 1] + 1)
        else:
            prefix_c[i] = prefix_c[i - 1]

        # Initialise maxi
    maxi = -sys.maxsize - 1

    # Check all the possibilities by
    # putting i and j at different
    # position & find maximum among them
    for i in range(N + 1):
        for j in range(i, N + 1):
            maxi = max(maxi,
                       (prefix_a[i] +
                        (prefix_b[j] -
                         prefix_b[i]) +
                        (prefix_c[N] -
                         prefix_c[j])))

        # Print the characters to be removed
    print((N - maxi))


# Driver Code
if __name__ == "__main__":
    # Given String
    st = "aaaabaaxccac"

    # Function Call
    min_remove(st)

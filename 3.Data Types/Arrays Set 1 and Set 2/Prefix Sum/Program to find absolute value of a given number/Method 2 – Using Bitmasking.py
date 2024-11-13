# Python3 program for Method 2
import sys

CHAR_BIT = 8


# Function to find the absolute value
def findAbsolute(N):
    # Find mask
    mask = N >> (sys.getsizeof(int()) // 8 * CHAR_BIT - 1)

    # Print the absolute value
    # by (mask + N)^mask
    print((mask + N) ^ mask)


# Driver Code
if __name__ == '__main__':
    # Given integer
    N = -12

    # Function call
    findAbsolute(N)



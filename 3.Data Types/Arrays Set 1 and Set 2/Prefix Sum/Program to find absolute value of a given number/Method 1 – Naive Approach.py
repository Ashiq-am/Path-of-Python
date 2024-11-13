# Python3 program for Method 1

# Function to find the absolute value
def findAbsolute(N):
    # If the number is less than
    # zero, then multiply by (-1)
    if (N < 0):
        N = (-1) * N

    # Print the absolute value
    print(N)


# Driver code
if __name__ == '__main__':
    # Given integer
    N = -12

    # Function call
    findAbsolute(N)



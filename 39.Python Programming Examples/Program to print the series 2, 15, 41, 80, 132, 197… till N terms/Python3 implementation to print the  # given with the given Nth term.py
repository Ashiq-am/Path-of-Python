# Python3 implementation to print the
# given with the given Nth term

# Function to print the series
def printSeries(N):
    ith_term = 0

    # Generate the ith term and
    for i in range(1, N + 1):
        ith_term = (13 * i * (i - 1)) / 2 + 2
        print(int(ith_term), ", ", end="")

    # Driver Code


if __name__ == '__main__':
    N = 7

    printSeries(N)



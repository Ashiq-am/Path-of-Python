# Python3 program for the above apporch

# Function to print the series
def PrintSeries(n):
    # Initialise the value of k with 2
    k = 2

    # Iterate from 1 to n
    for i in range(0, n):
        # Print each number
        print(k * (2 * k - 1), end=' ')

        # Increment the value of
        # K by 2 for next number
        k = k + 2


# Driver code

# Given number
n = 12

# Function Call
PrintSeries(n)

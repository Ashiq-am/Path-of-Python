# Python3 program to find sum of
# series of 1 + x^2 + x^3 + ....+ x^n

# Function to find the sum of
# the series and print N terms
# of the given series
def sum(x, n):
    total = 1.0
    multi = x

    # First Term
    print(1, end=" ")

    # Loop to print the N terms
    # of the series and find their sum
    for i in range(1, n):
        total = total + multi
        print('%.1f' % multi, end=" ")
        multi = multi * x

    print('\n')
    return total


# Driver code
x = 2
n = 5
print('%.2f' % sum(x, n))

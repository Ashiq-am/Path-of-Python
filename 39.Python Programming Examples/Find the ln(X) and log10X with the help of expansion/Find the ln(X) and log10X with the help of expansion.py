# Python 3 code to Find the ln x and
# log<sub>10</sub> x with the help of expansion
# Function to calculate ln x using expansion
from math import pow


def calculateLnx(n):
    sum = 0
    num = (n - 1) / (n + 1)

    # terminating value of the loop
    # can be increased to improve the precision
    for i in range(1, 1001, 1):
        mul = (2 * i) - 1
        cal = pow(num, mul)
        cal = cal / mul
        sum = sum + cal

    sum = 2 * sum
    return sum


# Function to calculate log10 x
def calculateLogx(lnx):
    return (lnx / 2.303)


# Driver Code
if __name__ == '__main__':
    n = 5
    lnx = calculateLnx(n)
    logx = calculateLogx(lnx)

    # setprecision(3) is used to display
    # the output up to 3 decimal places

    print("ln", "{0:.3f}".format(n),"=", "{0:.3f}".format(lnx))
    print("log10", "{0:.3f}".format(n),"=", "{0:.3f}".format(logx))

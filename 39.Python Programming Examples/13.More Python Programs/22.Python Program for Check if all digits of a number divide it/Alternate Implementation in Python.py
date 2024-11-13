# Python 3 program to
# check the number is
# divisible by all
# digits are not.

# Function to check
# the divisibility
# of the number by
# its digit.
def checkDivisibility(n, digit):
    # If the digit divides the
    # number then return true
    # else return false.
    return (digit != 0 and n % digit == 0)


# Function to check if
# all digits of n divide
# it or not
def allDigitsDivide(n):
    nlist = map(int, set(str(n)))
    for digit in nlist:
        if not (checkDivisibility(n, digit)):
            return False
    return True


# Driver function
n = 128

print("Yes" if (allDigitsDivide(n)) else "No")

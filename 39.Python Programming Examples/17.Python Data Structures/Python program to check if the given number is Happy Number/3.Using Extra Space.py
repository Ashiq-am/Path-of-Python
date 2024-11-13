# Method - returns true if the input is
# a happy number else returns false
def isHappynumber(n):
    if n == 1 or n == 7:
        return True

    Sum, x = n, n

    # This loop executes till the sum
    # of square of digits obtained is
    # not a single digit number
    while Sum > 9:
        Sum = 0

        # This loop finds the sum of
        # square of digits
        while x > 0:
            d = x % 10
            Sum += d * d
            x = int(x / 10)

        if Sum == 1:
            return True

        x = Sum

    if Sum == 7:
        return True

    return False


n = 13

if isHappynumber(n):
    print(n, "is a Happy number")
else:
    print(n, "is not a Happy number")

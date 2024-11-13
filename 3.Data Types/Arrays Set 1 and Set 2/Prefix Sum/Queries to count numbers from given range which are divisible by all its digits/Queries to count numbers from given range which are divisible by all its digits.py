# Python3 program to implement
# the above approach

# Function to check if a number is divisible
# by all of its non-zero digits or not
def CheckDivByAllDigits(number):
    # Stores the number
    n = number

    # Iterate over the digits
    # of the numbers
    while (n > 0):

        # If digit of number
        # is non-zero
        if (n % 10):

            # If number is not divisible
            # by its current digit
            if (number % (n % 10)):
                return False

        # Update n
        n //= 10
    return True


# Function to count of numbers which are
# divisible by all of its non-zero
# digits in the range [1, i]
def cntNumInRang(arr, N):
    global Max

    # Stores count of numbers which are
    # divisible by all of its non-zero
    # digits in the range [1, i]
    prefCntDiv = [0] * Max

    # Iterate over the range [1, Max]
    for i in range(1, Max):
        # Update
        prefCntDiv[i] = prefCntDiv[i - 1] + (CheckDivByAllDigits(i))

    # Traverse the array, arr[]
    for i in range(N):
        print(prefCntDiv[arr[i][1]] - prefCntDiv[arr[i][0] - 1], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [[1, 5], [12, 14]]
    Max = 1000005

    N = len(arr)
    cntNumInRang(arr, N)

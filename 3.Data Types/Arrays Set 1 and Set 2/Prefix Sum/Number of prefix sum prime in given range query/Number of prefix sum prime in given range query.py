# Python program to count the number
# of prefix sum which are prime or not
import numpy
import math


# Primality test to check if prefix
# sum is prime or not
def isPrime(num):
    # Corner case
    if (num <= 1):
        return False
    if (num <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (num % 2 == 0 or num % 3 == 0):
        return False

    for j in range(5, (int)(math.sqrt(num)) + 1, 6):
        if (num % j == 0 or num % (j + 2) == 0):
            return False

        return True

    # to calcluate the prefix sum for


# the given range of query
def primesubArraySum(arr, n, l, r, preSum):
    count = 0
    preSum[0] = arr[l]

    if (isPrime(preSum[0])):
        count = count + 1

    for i in range(l + 1, r):
        for j in range(1, n):
            preSum[j] = preSum[j - 1] + arr[i]

            # increase the count if the
            # prefix sum is prime
            if (isPrime(preSum[j])):
                count = count + 1

    return count


# Driver code
arr = [5, 7, 8, 10, 13]
n = len(arr)

# a = numpy.arange(5)
preSum = numpy.arange(n)
l = 0
r = 4
print(primesubArraySum(arr, n, l, r, preSum))



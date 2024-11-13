# Utility method to return
# sum of square of digits of n
def numSquareSum(n):
    squareSum = 0
    while n:
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum

# Method returns true if n is a Happy number
def isHappyNumber(n):
    slow = n
    fast = n
    while True:
        slow = numSquareSum(slow)
        fast = numSquareSum(numSquareSum(fast))
        if slow != fast:
            continue
        else:
            break
    return slow == 1

# Print all Happy Numbers between 1 and 100
for i in range(1, 101):
    if isHappyNumber(i):
        print(i, end=" ")

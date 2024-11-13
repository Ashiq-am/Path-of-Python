# Utility method to return sum of square of digits of n
def numSquareSum(n):
    squareSum = 0
    while n:
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum

# Method returns true if n is a Happy number
def isHappyNumber(n, visited):
    if n == 1:
        return True
    elif n in visited:
        return False
    else:
        visited.add(n)
        return isHappyNumber(numSquareSum(n), visited)

# Print all Happy Numbers between 1 and 100
for i in range(1, 101):
    visited = set()
    if isHappyNumber(i, visited):
        print(i, end=" ")

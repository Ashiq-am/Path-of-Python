# Python program for
# Efficient Solution to find
# find if count of divisors
# is even or odd

def NumOfDivisor(n):
    if n < 1:
        return
    root_n = n ** 0.5

    # If n is a perfect square,
    # then it has odd divisors
    if root_n ** 2 == n:
        print('Odd')
    else:
        print('Even')


# Driver code
if __name__ == '__main__':
    print("The count of divisor" +
          "of 10 is: ")
    NumOfDivisor(10)

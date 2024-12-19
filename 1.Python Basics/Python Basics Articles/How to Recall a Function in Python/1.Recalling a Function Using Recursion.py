def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recalling the function to calculate the factorial of 5
result = factorial(5)
print(result)
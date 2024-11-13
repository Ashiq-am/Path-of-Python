def factorial_iterative(n):
    accumulator = 1
    while n > 0:
        accumulator *= n
        n -= 1
    return accumulator

# Example usage
print(factorial_iterative(5))  # Output: 120

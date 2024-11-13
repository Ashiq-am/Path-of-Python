def fibonacci_tail_recursive(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_tail_recursive(n - 1, b, a + b)

# Example usage
print(fibonacci_tail_recursive(10))  # Output: 55

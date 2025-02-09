# Factorial function using recursion

# Base case: when n == 1, stop recursion
def factorial_rec(n):
    if n == 1:
        return 1  # Base case
    else:
        return n * factorial_rec(n - 1)  # Recursive case

# Example of recursion vs iteration

# Using recursion to find factorial
print(f"Factorial using recursion: {factorial_rec(5)}")


# Using iteration to find factorial
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial using iteration: {factorial_iter(5)}")

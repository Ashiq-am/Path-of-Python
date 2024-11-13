import timeit

# Inefficient memoized Fibonacci function
memo = {}


def fib_memoized(n):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memoized(n - 1) + fib_memoized(n - 2)
    return memo[n]


start_time = timeit.default_timer()
result = fib_memoized(30)
end_time = timeit.default_timer()
print("Time taken (Inefficient memoized):", end_time - start_time)

# Efficient recursive Fibonacci function


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


start_time = timeit.default_timer()
result = fib_recursive(30)
end_time = timeit.default_timer()
print("Time taken (Efficient recursive):", end_time - start_time)

# Without Yield (List-Based Approach)
import sys


def generate_squares_list(limit):
    squares = [num ** 2 for num in range(limit)]
    return squares

# With Yield (Generator-Based Approach)


def generate_squares_yield(limit):
    for num in range(limit):
        yield num ** 2


# Memory Comparison

limit = 10**6  # Set a large limit for demonstration purposes

# Without Yield (List-Based Approach)
squares_list = generate_squares_list(limit)
memory_usage_list = sys.getsizeof(squares_list)

# With Yield (Generator-Based Approach)
squares_yield = generate_squares_yield(limit)
memory_usage_yield = sys.getsizeof(squares_yield)

print(f"Memory usage without yield: {memory_usage_list} bytes")
print(f"Memory usage with yield: {memory_usage_yield} bytes")

import sys

# Define a generator function
def generate_numbers(n):
    for i in range(n):
        yield i


# Memory usage with traditional list creation
num_list = list(generate_numbers(1000000))
print("Memory usage with traditional list creation:", sys.getsizeof(num_list))
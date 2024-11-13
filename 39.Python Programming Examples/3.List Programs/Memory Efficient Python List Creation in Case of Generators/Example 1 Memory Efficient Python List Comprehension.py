import sys

# Define a generator function
def generate_numbers(n):
    for i in range(n):
        yield i

# Memory usage with list comprehension
num_list_comp = [num for num in generate_numbers(1000000)]
print("Memory usage with list comprehension:", sys.getsizeof(num_list_comp))
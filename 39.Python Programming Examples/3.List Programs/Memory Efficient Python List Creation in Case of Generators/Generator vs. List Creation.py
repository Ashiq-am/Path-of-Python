import sys

# Generator function
def generate_numbers(n):
    for i in range(n):
        yield i

# List comprehension method
num_list_comp = [i for i in generate_numbers(10000)]
size_list_comp = sys.getsizeof(num_list_comp)

# Direct conversion method
num_list = list(generate_numbers(10000))
size_list = sys.getsizeof(num_list)

# Calculate the difference
difference = size_list_comp - size_list

# Printing memory usage and difference
print("Memory usage of list comprehension:", size_list_comp, "bytes")
print("Memory usage of Generator:", size_list, "bytes")
print("Memory usage difference:", difference, "bytes")
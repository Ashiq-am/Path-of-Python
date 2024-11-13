# Define a generator function
def generate_numbers(n):
    for i in range(n):
        yield i


# Create a list using list comprehension
num_list = [num for num in generate_numbers(1000000)]
# Print the first 10 elements of the list
print(num_list[:10])
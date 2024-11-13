# Python code to demonstrate the working of
# dropwhile()


# Function to be passed
# as an argument
def is_positive(n):
	return n > 0

value_list =[5, 6, -8, -4, 2]
result = list(itertools.dropwhile(is_positive, value_list))

print(result)

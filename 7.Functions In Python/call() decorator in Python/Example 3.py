# Helper function to build a
# list of numbers
def list_of_numbers(n):
	element = []
	for i in range(n):
		element.append(i * 2)
	return element

list_of_numbers = list_of_numbers(6)

# Output command
print(len(list_of_numbers),
	list_of_numbers[2])

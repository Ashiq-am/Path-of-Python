# Declare a list to store integers
array = []

# Read the size of the array
n = int(input())

# Taking input in the list
for i in range(n):
	element = int(input())
	array.append(element)

# Accessing the i'th element of the list
i = 5
if 0 <= i < len(array):
	x = array[i]
	print(f"The element at index {i} is: {x}")
else:
	print("Index out of bounds.")

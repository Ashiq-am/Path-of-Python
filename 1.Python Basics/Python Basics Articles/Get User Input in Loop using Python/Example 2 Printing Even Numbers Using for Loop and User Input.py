# the user to input a series of numbers separated by spaces
user_input = input()

# Split the input string into individual numbers and convert each to an integer
numbers = [int(num) for num in user_input.split()]

# Initialize an empty list to store even numbers
even_numbers = []

# Iterate through the numbers using a for loop
for num in numbers:
	if num % 2 == 0:
		even_numbers.append(num)

# Print the list of even numbers
print("Even numbers from the input:", even_numbers)

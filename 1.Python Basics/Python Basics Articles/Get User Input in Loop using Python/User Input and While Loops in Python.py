# Initializing an empty list to store numbers
number_list = []

# Prompting the user to enter numbers
while True:
	num = input("Enter a number (or 'done' to finish): ")
	if num == 'done':
		break
	number_list.append(int(num))

# Printing the list of numbers
print("List of numbers:", number_list)

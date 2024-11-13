# Initialize an empty list to store inputs
inputs_list = []

# Set the initial value for the input
user_input = input("Enter a value (type 'exit' to stop): ")

# Use a while loop to continue taking inputs until 'exit' is entered
while user_input.lower() != 'exit':
	inputs_list.append(user_input)
	user_input = input("Enter another value (type 'exit' to stop): ")

# Display the collected inputs
print("Collected Inputs:", inputs_list)

# Using a List and For Loop
num_inputs = int(input("Enter the number of inputs: "))
user_inputs = []

for i in range(num_inputs):
	user_input = input(f"Enter input {i + 1}: ")
	user_inputs.append(user_input)

print("User inputs:", user_inputs)

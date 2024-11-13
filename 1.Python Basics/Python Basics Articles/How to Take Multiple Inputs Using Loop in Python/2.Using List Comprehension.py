# Using List Comprehension
num_inputs = int(input("Enter the number of inputs: "))
user_inputs = [input(f"Enter input {i + 1}: ") for i in range(num_inputs)]

print("User inputs:", user_inputs)

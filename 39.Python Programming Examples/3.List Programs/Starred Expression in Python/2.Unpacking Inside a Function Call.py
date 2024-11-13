# Example list
grades = [90, 85, 88, 92, 95]

# Define a function that takes individual arguments

def calculate_average(first, *others):
	total = first + sum(others)
	average = total / (1 + len(others))
	return average

# Unpack the list inside the function call
average_grade = calculate_average(*grades)

# Print the result
print("Average Grade:", average_grade)

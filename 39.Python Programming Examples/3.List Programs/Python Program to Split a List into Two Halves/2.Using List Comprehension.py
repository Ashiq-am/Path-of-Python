def split_list(input_list):
	middle = len(input_list) // 2
	first_half = [input_list[i] for i in range(middle)]
	second_half = [input_list[i] for i in range(middle, len(input_list))]
	return first_half, second_half

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
output = split_list(my_list)
print("\List Comprehension:")
print("First Half:", output[0])
print("Second Half:", output[1])

def split_list(input_list):
	middle = len(input_list) // 2
	first_half = []
	second_half = []
	for i in range(middle):
		first_half.append(input_list[i])
	for i in range(middle, len(input_list)):
		second_half.append(input_list[i])
	return first_half, second_half

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
output = split_list(my_list)
print("\Iterative:")
print("First Half:", output[0])
print("Second Half:", output[1])

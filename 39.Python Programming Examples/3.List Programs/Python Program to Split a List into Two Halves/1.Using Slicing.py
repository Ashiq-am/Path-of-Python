def split_list_slicing(input_list):
	length = len(input_list)
	middle = length // 2
	first_half = input_list[:middle]
	second_half = input_list[middle:]
	return first_half, second_half

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
output = split_list_slicing(my_list)
print("Slicing:")
print("First Half:", output[0])
print("Second Half:", output[1])

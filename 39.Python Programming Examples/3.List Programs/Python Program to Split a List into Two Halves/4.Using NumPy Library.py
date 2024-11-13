import numpy as np

def split_list(input_list):
	array_list = np.array(input_list)
	middle = len(array_list) // 2
	first_half = array_list[:middle].tolist()
	second_half = array_list[middle:].tolist()
	return first_half, second_half

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
output = split_list(my_list)
print("\nNumPy:")
print("First Half:", output[0])
print("Second Half:", output[1])

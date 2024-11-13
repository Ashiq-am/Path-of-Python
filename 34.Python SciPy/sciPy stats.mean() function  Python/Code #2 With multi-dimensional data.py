# Arithmetic Mean

from scipy import mean

arr1 = [[1, 3, 27],
		[3, 4, 6],
		[7, 6, 3],
		[3, 6, 8]]

print("Arithmetic Mean is :", mean(arr1))

# using axis = 0
print("\nArithmetic Mean is with default axis = 0 : \n",
	mean(arr1, axis = 0))

# using axis = 1
print("\nArithmetic Mean is with default axis = 1 : \n",
	mean(arr1, axis = 1))

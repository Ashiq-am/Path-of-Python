def double(integer):
	return integer*2


# driver code
integer_list = [1, 2, 3]

# Calling double method on each integer
# in list using list comprehension.
output_list = [double(i) for i in integer_list]

print(output_list)

def double(integer):
	return integer*2


# driver code
integer_list = [1, 2, 3]

# Map method returns a map object
# so we cast it into list using list()
output_list = list(map(double, integer_list))

print(output_list)

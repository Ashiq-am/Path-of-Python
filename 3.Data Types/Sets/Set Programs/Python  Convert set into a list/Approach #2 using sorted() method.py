# Python3 program to convert a
# set into a list
def convert(set):
	return sorted(set)

# Driver function
my_set = {1, 2, 3}

s = set(my_set)
print(convert(s))

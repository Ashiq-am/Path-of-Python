# Python3 program to convert a
# list into a tuple
def convert(list):
	return (*list, )

# Driver function
list = [1, 2, 3, 4]
print(convert(list))

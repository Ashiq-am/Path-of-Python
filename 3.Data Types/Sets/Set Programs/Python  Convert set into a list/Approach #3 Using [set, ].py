# Python3 program to convert a
# set into a list
def convert(set):
	return [*set, ]

# Driver function
s = set({1, 2, 3})
print(convert(s))

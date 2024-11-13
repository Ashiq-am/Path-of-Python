# Python3 program to Convert positive
# list integers to negative and vice-versa
def Convert(lst):
	return [ -i for i in lst ]

# Driver code
lst = [-1, 2, 3, -4, 5, -6, -7]
print(Convert(lst))

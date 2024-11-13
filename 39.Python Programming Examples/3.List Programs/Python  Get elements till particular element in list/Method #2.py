# Python3 code to demonstrate working of
# Get elements till particular element in list
# using generator

# helper function to perform task
def print_ele(test_list, val):
	for ele in test_list:
		if ele == val:
			return
		yield ele

# initialize list
test_list = [1, 4, 6, 8, 9, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# declaring elements till which elements required
N = 8

# Get elements till particular element in list
# using generator
res = list(print_ele(test_list, N))

# printing result
print("Elements till N in list are : " + str(res))

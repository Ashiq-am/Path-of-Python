# Python3 code to demonstrate working of
# Squash consecutive values of K
# Using yield + groupby()
import itertools

# helper function
def hlper_fnc(test_list, K):
	for key, val in itertools.groupby(test_list):
		if key == K:
			yield key
		else:
			yield from val

# initializing list
test_list = [4, 5, 5, 4, 3, 3, 5, 5, 5, 6, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# Squash consecutive values of K
# Using yield + groupby()
res = list(hlper_fnc(test_list, K))

# printing result
print("List after filteration : " + str(res))

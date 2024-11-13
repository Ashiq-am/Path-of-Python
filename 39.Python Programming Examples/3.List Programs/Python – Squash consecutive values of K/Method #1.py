# Python3 code to demonstrate working of
# Squash consecutive values of K
# Using zip() + yield

# helper function
def hlper_fnc(test_list, K):
	for sub1, sub2 in zip(test_list, test_list[1:]):
		if sub1 == sub2 == K:
			continue
		else:
			yield sub1
	yield sub2

# initializing list
test_list = [4, 5, 5, 4, 3, 3, 5, 5, 5, 6, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# Squash consecutive values of K
# Using zip() + yield
res = list(hlper_fnc(test_list, K))

# printing result
print("List after filteration : " + str(res))

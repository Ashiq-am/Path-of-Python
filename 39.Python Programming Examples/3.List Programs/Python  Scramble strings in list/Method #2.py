# Python3 code to demonstrate working of
# Scramble strings in list
# using list comprehension + shuffle() + join()
from random import shuffle

# Utility function
def perform_scramble(ele):
	ele = list(ele)
	shuffle(ele)
	return ''.join(ele)

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Scramble strings in list
# using list comprehension + shuffle() + join()
res = [perform_scramble(ele) for ele in test_list]

# printing result
print("Scrambled strings in lists are : " + str(res))

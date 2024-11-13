# Python3 code to demonstrate working of
# Filter Strings combination of K substrings
# Using permutations() + map() + join() + set() + intersection()
from itertools import permutations

# initializing list
test_list = ["geeks4u", "allbest", "abcdef"]

# printing string
print("The original list : " + str(test_list))

# initializing substring list
substr_list = ["s4u", "est", "al", "ge", "ek", "def", "lb"]

# initializing K
K = 3

# getting all permutations
perms = set(map(''.join, permutations(substr_list, r = K)))

# using intersection() to solve this problem
res = list(set(test_list).intersection(perms))

# printing results
print("Strings after joins : " + str(res))

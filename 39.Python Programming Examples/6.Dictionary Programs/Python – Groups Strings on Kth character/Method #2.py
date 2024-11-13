# Python3 code to demonstrate working of
# Groups Strings on Kth character
# Using loop + map()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Groups Strings on Kth character
# Using loop + map()
res = dict()
for char in map(chr, range(97, 123)):
	words = [idx for idx in test_list if idx[K - 1] == char]
	if words:
		res[char] = words

# printing result
print("The strings grouping : " + str(res))

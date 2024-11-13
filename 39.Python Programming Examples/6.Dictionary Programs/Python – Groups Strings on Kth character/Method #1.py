# Python3 code to demonstrate working of
# Groups Strings on Kth character
# Using loop
from collections import defaultdict

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Groups Strings on Kth character
# Using loop
res = defaultdict(list)
for word in test_list:
	res[word[K - 1]].append(word)

# printing result
print("The strings grouping : " + str(dict(res)))

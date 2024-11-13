# Python3 code to demonstrate working of
# Most frequent word in Strings List
# Using loop + max() + split() + defaultdict()
from collections import defaultdict

# initializing Matrix
test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

# printing original list
print("The original list is : " + str(test_list))

temp = defaultdict(int)

# memoizing count
for sub in test_list:
	for wrd in sub.split():
		temp[wrd] += 1

# getting max frequency
res = max(temp, key=temp.get)

# printing result
print("Word with maximum frequency : " + str(res))

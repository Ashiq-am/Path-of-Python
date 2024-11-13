# Python3 code to demonstrate working of
# Character repetition string combinations
# Using join() + nested loop + list comprehension + * operator

# initializing list
test_list = ["gfg", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# repeat list
rep_list = [3, 5, 2]

# * operator performs repetitions
# list comprehension encapsulates logic
res = [''.join(sub * ele1 for sub in ele2)
	for ele1 in rep_list for ele2 in test_list]

# printing result
print("All repetition combinations strings : " + str(res))

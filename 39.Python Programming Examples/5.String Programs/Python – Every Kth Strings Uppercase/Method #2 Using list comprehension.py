# Python3 code to demonstrate working of
# Every Kth Strings Uppercase
# Using list comprehension

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks", "and", "CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# shorthand to perform this task
res = [test_list[idx].upper() if idx % K == 0 else test_list[idx]
	for idx in range(len(test_list))]

# printing result
print("The resultant String list : " + str(res))

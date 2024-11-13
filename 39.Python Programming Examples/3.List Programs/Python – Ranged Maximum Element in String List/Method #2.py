# Python3 code to demonstrate working of
# Ranged Maximum Element in String Matrix
# Using generator expression + max()

# initializing list
test_list = ['34, 78, 98, 23, 12',
			'76, 65, 54, 43, 21',
			'82, 45, 32, 45, 32',
			'78, 34, 12, 34, 10']

# printing original list
print("The original list is : " + str(test_list))

# initializing Range
i, j = 2, 4

# Ranged Maximum Element in String Matrix
# Using generator expression + max()
res = max(ele for sub in test_list for ele in sub.split(', ')[i - 1: j])

# printing result
print("The maximum ranged element : " + str(res))

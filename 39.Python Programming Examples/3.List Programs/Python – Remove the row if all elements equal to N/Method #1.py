# Python3 code to demonstrate
# N row deletion in Matrix
# using list comprehension + count() + len()

# initializing matrix
test_list = [[1, 4, 2], [False, 9, 3],
			[6, 6, 6], [1, 0, 1]]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 6

# using list comprehension + count() + len()
# N row deletion in Matrix
res = [sub for sub in test_list if sub.count(N) != len(sub)]

# print result
print("The list after removal of N rows : " + str(res))

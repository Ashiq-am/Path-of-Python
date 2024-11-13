# Python3 code to demonstrate
# alternate range slicing
# using list comprehension

# initializing list
test_list = [2, 4, 6, 8, 9, 10, 12, 16, 18, 20, 7, 30]

# printing original list
print("The original list : " + str(test_list))

# Select range size
N = 3

# using list comprehension
# alternate range slicing
res = [test_list[i] for i in range(len(test_list))
							if i % (N * 2) >= N]

# print result
print("The alternate range sliced list : " + str(res))

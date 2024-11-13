# Python3 code to demonstrate
# group flattening of list
# using list comprehension + zip() + map()

# initializing list of lists
test_list = [[1, 3], [3, 4], [6, 5], [4, 5], [7, 6], [7, 9]]

# printing original list
print("The original list : " + str(test_list))

# declaring K
K = 3

# using list comprehension + zip() + map()
# group flattening of list
res = list(map(list, zip(*[iter([i for sub in test_list
			for i in sub])]*(K * len(test_list[0])))))

# printing result
print("The grouped flattened list : " + str(res))

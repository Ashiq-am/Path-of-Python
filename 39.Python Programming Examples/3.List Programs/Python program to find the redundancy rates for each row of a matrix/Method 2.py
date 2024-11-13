# initializing list
test_list = [[4, 5, 2, 4, 3], [5, 5, 5, 5, 5],
			[8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension for one liner
res = [1 - len(set(sub)) / len(sub) for sub in test_list]

# printing result
print("Matrix Redundancy ? : " + str(res))

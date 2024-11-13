# initializing list
test_list = [1, 2, 4, 2, 6, 7, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# one-liner alternative
res = len([test_list[idx] for idx in range(1, len(test_list) - 1) if test_list[idx + 1] >
		test_list[idx] < test_list[idx - 1] or test_list[idx + 1] < test_list[idx] > test_list[idx - 1]])

# printing result
print("Peaks and Valleys count : " + str(res))

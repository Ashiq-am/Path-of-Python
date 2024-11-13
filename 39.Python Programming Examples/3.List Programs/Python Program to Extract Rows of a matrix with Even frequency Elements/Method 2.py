from collections import Counter

# initializing list
test_list = [[4, 5, 5, 2], [4, 4, 4, 4, 2, 2],
			[6, 5, 6, 5], [1, 2, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# Counter() gets the required frequency
# filter() used to perform filtering
res = list(filter(lambda sub: all(val % 2 == 0 for key,
								val in list(dict(Counter(sub)).items())), test_list))

# printing result
print("Filtered Matrix ? : " + str(res))

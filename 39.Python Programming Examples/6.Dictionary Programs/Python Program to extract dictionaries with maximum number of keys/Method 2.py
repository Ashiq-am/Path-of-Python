# initializing list
test_list = [{'Gfg': 1}, {'Gfg': 1, 'is': 5, 'best': 4},
			{'Gfg': 2, 'best': 9, "book": 1}]

# printing original list
print("The original list is : " + str(test_list))

max_len = max(len(sub) for sub in test_list)
res = [sub for sub in test_list if len(sub) == max_len]

# printing result
print("Dictionary with maximum keys : " + str(res))

# Python3 code to demonstrate working of
# Alternate Elements Dictionary
# Using loop

# initializing list
test_list = [2, 3, 5, 6, 7, 8, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

res = dict()

# pairing first set of Alternate elements
for idx in range(len(test_list) - 2):
	if idx % 2:
		res[test_list[idx]] = test_list[idx + 2]

# pairing other set
for idx in range(len(test_list) - 2):
	if not idx % 2:
		res[test_list[idx]] = test_list[idx + 2]

# printing result
print("The extracted dictionary : " + str(res))

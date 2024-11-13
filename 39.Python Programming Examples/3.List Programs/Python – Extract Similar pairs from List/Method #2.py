# Python3 code to demonstrate working of
# Extract Similar pairs from List
# Using fromkeys() + list comprehension

# initializing list
test_list = [4, 6, 7, 4, 2, 6, 2, 8]

# printing original list
print("The original list is : " + str(test_list))

# Extract Similar pairs from List
# Using fromkeys() + list comprehension
temp = dict.fromkeys(test_list, 0)
for key in test_list:
	temp[key] += 1
res = [(key, key) for key, val in temp.items() for _ in range(val // 2)]

# printing result
print("The records after pairing : " + str(res))

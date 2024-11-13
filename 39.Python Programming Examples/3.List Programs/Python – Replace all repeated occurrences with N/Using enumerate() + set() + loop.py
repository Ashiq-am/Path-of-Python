# Python3 code to demonstrate
# Replace all repeated occurrences of K with N
# using enumerate() + set() + loop

# Initializing list
test_list = [1, 3, 3, 1, 4, 4, 1, 5, 5]

# printing original list
print("The original list is : " + str(test_list))

# Initializing N
N = 'rep'

# Replace all repeated occurrences of K with N
# using enumerate() + set() + loop
his = set([])
for idx, ele in enumerate(test_list):
	if ele in his:
		test_list[idx] = N
	his.add(ele)

# printing result
print ("The duplication altered list : " + str(test_list))

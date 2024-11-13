# Python3 code to demonstrate working of
# Next different element in list
# Using set() + sorted() + index()

# initializing list
test_list = [3, 4, 6, 6, 3, 2, 3, 5, 6, 3, 4, 5, 5, 3, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing element
nex_to_ele = 6

# sorting removing duplicated keeping order
temp = sorted(set(test_list), key=lambda sub: test_list.index(sub))

# getting next index
num_idx = temp.index(nex_to_ele)

# checking for last index for overflow
if num_idx == len(temp) - 1:
	res = None

# getting next index as result
else:
	res = temp[num_idx + 1]

# printing result
print("Next different element : " + str(res))

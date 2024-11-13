# Python3 code to demonstrate working of
# Next different element in list
# Using next() + iter() + sorted() + set()

# initializing list
test_list = [3, 4, 6, 6, 3, 2, 3, 5, 6, 3, 4, 5, 5, 3, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing element
nex_to_ele = 6

# sorting removing duplicated keeping order
temp = sorted(set(test_list), key=lambda sub: test_list.index(sub))

temp_itr = iter(temp)
flag = 0
for idx in range(0, len(temp)):

	# if last element is element to find
	if idx == len(temp) - 1:
		flag = 1

	# breaking when element is found
	if next(temp_itr) == nex_to_ele:
		break

if flag:
	res = None
else:

	# next element is answer
	res = next(temp_itr)

# printing result
print("Next different element : " + str(res))

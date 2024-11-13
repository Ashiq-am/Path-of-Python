# Python3 code to demonstrate working of
# Selective Merge list every Nth position
# using loop + extend() + iter() + next()

# initialize lists
test_list1 = [1, 4, 9, 10, 19, 65, 78, 23, 78]
test_list2 = [8, 14, 50]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Selective Merge list every Nth position
# using loop + extend() + iter() + next()
N = 3
temp_iter = iter(test_list1)
res = []
for ele in test_list2:
	res.extend([next(temp_iter) for _ in range(N - 1)])
	res.append(ele)
res.extend(temp_iter)

# printing result
print("The List after merge is : " + str(res))

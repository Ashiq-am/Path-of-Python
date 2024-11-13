# Python3 code to demonstrate working of
# Selective Merge in String list
# using list comprehension + join() + zip()

# initialize lists
test_list1 = ["abc", "de", "efgh"]
test_list2 = ["gfg", "is", "good"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initialize exempt char
exm_chr = 'g'

# Selective Merge in String list
# using list comprehension + join() + zip()
res = [''.join(l if l == exm_chr else k for k, l in zip(i, j))
	for i, j in zip(test_list1, test_list2)]

# printing result
print("The resultant list after Selective Merge : " + str(res))

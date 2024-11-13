# Python3 code to demonstrate working of
# Selective Merge in String list
# using map() + lambda() + join() + zip()

# initialize lists
test_list1 = ["abc", "de", "efgh"]
test_list2 = ["gfg", "is", "good"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initialize exempt char
exm_chr = 'g'

# Selective Merge in String list
# using map() + lambda() + join() + zip()
temp = lambda ele: ''.join([i if j != exm_chr else j for i, j in ele])
res = list(map(temp, (map(lambda k: zip(*k), zip(test_list1, test_list2)))))

# printing result
print("The resultant list after Selective Merge : " + str(res))

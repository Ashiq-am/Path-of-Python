# Python3 code to demonstrate working of
# Compare Unordered Dictionary List
# Using sorted() + key + lambda

# initializing lists
test_list1 = [{'Manjeet' : 12, 'Himani' : 15}, {'Akshat' : 20, 'Vashu' : 15}]
test_list2 = [{'Vashu' : 15, 'Akshat' : 20}, {'Himani' : 15, 'Manjeet' : 12}]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Compare Unordered Dictionary List
# Using sorted() + key + lambda
res = sorted(test_list1, key = lambda ele: sorted(ele.items())) == sorted(
						test_list2, key = lambda ele: sorted(ele.items()))

# printing result
print("Are Dictionary Lists equal ? : " + str(res))

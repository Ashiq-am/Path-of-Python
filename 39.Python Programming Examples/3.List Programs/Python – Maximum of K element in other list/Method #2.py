# Python3 code to demonstrate working of
# Maximum of K element in other list
# Using list comprehension + max() + zip()

# initializing lists
test_list1 = [4, 3, 6, 2, 9]
test_list2 = [3, 6, 3, 4, 3]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 3

# one liner to solve this problem
res = max([sub1 for sub1, sub2 in zip(test_list1, test_list2) if sub2 == K])

# printing result
print("Extracted Maximum element : " + str(res))

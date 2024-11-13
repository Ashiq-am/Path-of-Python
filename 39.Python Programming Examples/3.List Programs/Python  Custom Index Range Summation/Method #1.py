# Python3 code to demonstrate
# Custom Index Range Summation
# using list comprehension + zip() + sum()

# initializing string
test_list = [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]

# initializing split index list
split_list = [2, 5, 7]

# printing original list
print ("The original list is : " + str(test_list))

# printing original split index list
print ("The original split index list : " + str(split_list))

# using list comprehension + zip() + sum()
# Custom Index Range Summation
res = [sum(test_list[i : j]) for i, j in zip([0] +
				split_list, split_list + [None])]

# printing result
print ("The splitted lists summation are : " + str(res))

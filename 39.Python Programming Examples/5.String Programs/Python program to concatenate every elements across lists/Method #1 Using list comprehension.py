# Python3 code to demonstrate working of
# All elements concatenation across lists
# Using list comprehension

# initializing lists
test_list1 = ["gfg", "is", "best"]
test_list2 = ["love", "CS"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# forming pairs
temp = [(a, b) for a in test_list1 for b in test_list2]

# performing concatenation
res = [x + ' ' + y for (x, y) in temp]

# printing result
print("The paired combinations : " + str(res))

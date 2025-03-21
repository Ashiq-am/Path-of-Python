# Python3 code to demonstrate
# Consecutive Pairs Duplication Removal
# using list comprehension + zip() + map()

# Initializing lists
test_list1 = [1, 2, 3, 4, 5]
test_list2 = [2, 3, 4, 5, 6]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Consecutive Pairs Duplication Removal
# using list comprehension + zip() + map()
res = "[" + " ".join(map(str, zip(test_list1, test_list2))) + "]"

# printing result
print("The combined list after consecutive comma removal : " + str(res))

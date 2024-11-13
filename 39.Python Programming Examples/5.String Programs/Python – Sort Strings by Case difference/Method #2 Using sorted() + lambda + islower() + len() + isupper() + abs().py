# Python3 code to demonstrate working of
# Python3 code to demonstrate working of
# Sort Strings by Case difference
# Using sorted() + lambda + islower() + len() + isupper() + abs()

# initializing Matrix
test_list = ["GFG", "GeeKs", "best", "FOr", "alL", "GEEKS"]

# printing original list
print("The original list is : " + str(test_list))

# sorting using sorted()
# lambda function to inject functionality
res = sorted(test_list, key=lambda string: \
    abs(len([ele for ele in string if ele.islower()]) - \
        len([ele for ele in string if ele.isupper()])))

# printing result
print("Sorted Strings by case difference : " + str(res))

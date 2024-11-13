# Python3 code to demonstrate working of
# Substring Intersections
# Using any() + generator expression

# initializing lists
test_list1 = ["Geeksforgeeks", "best", "for", "geeks"]
test_list2 = ["Geeks", "win", "or", "learn"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# any() returns the string after match in any string
# as Substring
res = [ele2 for ele2 in test_list2 if any(ele2 in ele1 for ele1 in test_list1)]

# printing result
print("Substrings Intersections : " + str(res))

# Python3 code to demonstrate working of
# Substring Intersections
# Using list comprehension

# initializing lists
test_list1 = ["Geeksforgeeks", "best", "for", "geeks"]
test_list2 = ["Geeks", "win", "or", "learn"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using list comprehension for nested loops
res = list(
	set([ele1 for sub1 in test_list1 for ele1 in test_list2 if ele1 in sub1]))

# printing result
print("Substrings Intersections : " + str(res))

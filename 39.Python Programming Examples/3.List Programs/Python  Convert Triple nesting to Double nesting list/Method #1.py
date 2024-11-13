# Python3 code to demonstrate working of
# Convert Triple nesting to Double nesting list
# using list comprehension

# initialize list
test_list = [[[1, 4, 6]], [[8, 9, 10, 7]]]

# printing original list
print("The original list is : " + str(test_list))

# Convert Triple nesting to Double nesting list
# using list comprehension
res = [sub[0] for sub in test_list]

# printing result
print("Double nested list from triple nested : " + str(res))

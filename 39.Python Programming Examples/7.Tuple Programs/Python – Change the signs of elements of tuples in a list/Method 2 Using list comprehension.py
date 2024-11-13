# initializing lists
test_list = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9, -3)]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension used as one liner
res = [(abs(sub[0]), -abs(sub[1])) for sub in test_list]

# printing result
print("Updated Tuple list : " + str(res))

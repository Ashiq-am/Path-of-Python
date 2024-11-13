# initializing list
test_list = [{1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}, {6: 5, 9: 3, 1: 6}]

# printing original list
print("The original list is : " + str(test_list))

# sorting dictionary list by maximum value
# one statement sort
res = sorted(test_list, key=lambda dicts: max(list(dicts.values())))

# printing result
print("Sorted List : " + str(res))

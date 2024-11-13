# Python code to demonstrate working of
# Check if two list of tuples are identical
# using cmp()

# initialize list of tuples
test_list1 = [(10, 4), (2, 5)]
test_list2 = [(10, 4), (2, 5)]

# printing original tuples lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Check if two list of tuples are identical
# using cmp()
res = not cmp(test_list1, test_list2)

# printing result
print("Are tuple lists identical ? : " + str(res))

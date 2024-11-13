# Python3 code to demonstrate working of
# Elements Lengths in List
# Using list comprehension + len()

# initializing list
test_list = ['GFG', (4, 5, 6), 17, [5, 6, 7, 8], 'Best']

# printing original list
print("The original list is : " + str(test_list))

# Elements Lengths in List
# Using list comprehension + len()
res = [len(sub) if type(sub) != int else 1 for sub in test_list]

# printing result
print("The element sizes in order are : " + str(res))

# Python3 code to demonstrate working of
# Convert Uneven Lists into Records
# Using list comprehension + zip()

# initializing lists
test_list1 = ['Nikhil', 'Akash', 'Akshat']
test_list2 = [5, 6, 7, 8, 2, 3, 12, 2, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Convert Uneven Lists into Records
# Using list comprehension + zip()
temp = len(test_list2) // len(test_list1)
res = [test_list2[idx :: temp] for idx in range(0, len(test_list1))]
res = dict(zip(test_list1, res))

# printing result
print("The paired data dictionary : " + str(res))

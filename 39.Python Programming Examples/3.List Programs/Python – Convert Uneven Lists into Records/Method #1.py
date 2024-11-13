# Python3 code to demonstrate working of
# Convert Uneven Lists into Records
# Using dictionary comprehension + enumerate() + list slicing

# initializing lists
test_list1 = ['Nikhil', 'Akash', 'Akshat']
test_list2 = [5, 6, 7, 8, 2, 3, 12, 2, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Convert Uneven Lists into Records
# Using dictionary comprehension + enumerate() + list slicing
temp = len(test_list2) // len(test_list1)
res = {key: test_list2[idx :: temp] for idx, key in enumerate(test_list1)}

# printing result
print("The paired data dictionary : " + str(res))

# Python3 code to demonstrate working of
# Alternate Elements Dictionary
# Using dictionary comprehension + list slicing

# initializing list
test_list = [2, 3, 5, 6, 7, 8, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

# extracting lists
list1 = test_list[1::2]
list2 = test_list[::2]

# constructing pairs using dictionary comprehension
res = {list1[idx] : list1[idx + 1] for idx in range(len(list1) - 1)}
res.update({list2[idx] : list2[idx + 1] for idx in range(len(list2) - 1)})

# printing result
print("The extracted dictionary : " + str(res))

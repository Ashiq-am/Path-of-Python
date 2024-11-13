# Python3 code to demonstrate
# Every Kth element removal in List
# using list comprehension + list slicing

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using list comprehension + list slicing
# Every Kth element removal in List
# removes every 3rd element
res = [i for i in test_list if i not in test_list[0 :: 3]]

# printing result
print ("The list after removing every Kth element : " + str(res))

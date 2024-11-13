# Python3 code to demonstrate
# Every Kth element removal in List
# using list comprehension + enumerate()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using list comprehension + enumerate()
# Every Kth element removal in List
# Remove every third element
res = [i for j, i in enumerate(test_list) if j % K != 0]

# printing result
print ("The list after removing every Kth element : " + str(res))

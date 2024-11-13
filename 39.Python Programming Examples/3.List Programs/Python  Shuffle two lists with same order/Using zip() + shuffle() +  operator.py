# Python3 code to demonstrate working of
# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
import random

# initializing lists
test_list1 = [6, 4, 8, 9, 10]
test_list2 = [1, 2, 3, 4, 5]

# printing lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
temp = list(zip(test_list1, test_list2))
random.shuffle(temp)
res1, res2 = zip(*temp)

# Printing result
print("List 1 after shuffle : " + str(list(res1)))
print("List 2 after shuffle : " + str(list(res2)))

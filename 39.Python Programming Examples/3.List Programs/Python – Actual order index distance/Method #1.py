# Python3 code to demonstrate
# Actual order index distance
# using sorted() + index() + list comprehension

# initializing list
test_list = [6, 3, 1, 2, 5, 4]

# printing original list
print("The original list is : " + str(test_list))

# using sorted() + index() + list comprehension
# Actual order index distance
temp = sorted(test_list)
res = [abs(temp.index(ele) - idx) for idx, ele in enumerate(test_list)]

# printing result
print ("The relative ordering list is : " + str(res))

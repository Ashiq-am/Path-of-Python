# Python3 code to demonstrate
# Finding relative order of elements in list
# using sorted() + index() + list comprehension

# initializing list
test_list = [6, 3, 1, 2, 5, 4]

# printing original list
print("The original list is : " + str(test_list))

# using sorted() + index() + list comprehension
# Finding relative order of elements in list
temp = sorted(test_list)
res = [temp.index(i) for i in test_list]

# printing result
print ("The relative ordering list is : " + str(res))

# Python code to demonstrate
# to construct alternate element list
# using list comprehension

# initializing list
test_list = [1, 4, 6, 7, 9, 3, 5]

# printing original list
print ("The original list : " + str(test_list))

# using list comprehension
# to construct alternate element list
res = [test_list[i] for i in range(len(test_list)) if i % 2 != 0]

# printing result
print ("The alternate element list is : " + str(res))

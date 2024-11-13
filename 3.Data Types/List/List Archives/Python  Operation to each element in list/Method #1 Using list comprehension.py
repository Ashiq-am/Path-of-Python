# Python3 code to demonstrate
# operations on each list element
# using list comprehension

# initializing list
test_list = ["geeks", "for", "geeks", "is", "best"]

# printing original list
print ("The original list is : " + str(test_list))

# operations on each list element
# using list comprehension
# uppercasing each element
res = [i.upper() for i in test_list]

# printing result
print ("The uppercased list is : " + str(res))

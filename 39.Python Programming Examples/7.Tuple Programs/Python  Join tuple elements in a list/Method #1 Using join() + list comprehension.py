# Python3 code to demonstrate
# joining tuple elements
# using join() + list comprehension

# initializing tuple list
test_list = [('geeks', 'for', 'geeks'),
			('computer', 'science', 'portal')]

# printing original list
print ("The original list is : " + str(test_list))

# using join() + list comprehension
# joining tuple elements
res = [' '.join(tups) for tups in test_list]

# printing result
print ("The joined data is : " + str(res))

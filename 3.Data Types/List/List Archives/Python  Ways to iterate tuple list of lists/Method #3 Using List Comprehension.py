# Python code to demonstrate ways to
# iterate tuples list of list into single
# list using list comprehension

# initialising listoflist
test_list = [
		[('11'), ('12'), ('13')],
		[('21'), ('22'), ('23')],
		[('31'), ('32'), ('33')]
		]


# printing intial list
print ("Initial List = ", test_list)

# iterate list tuples list of list into single list
# using list comprehension
res_list = [item for list2 in test_list for item in list2]

# print final List
print ("Resultant List = ", res_list)

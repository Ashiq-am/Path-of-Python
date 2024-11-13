# Python3 code to demonstrate
# segragation of keys and values
# using map() + list() + zip()

# initializing list of dictionaries
test_list = [{'Nikhil' : 1, 'Akash' : 2},
			{'Nikhil' : 3, 'Akash' : 4}]

# printing original list
print("The original list : " + str(test_list))

# using map() + list() + zip()
# to segregate keys and values
res = list(zip(*map(dict.values, test_list)))

# printing result
print("The segregated keys and values : " + str(res))

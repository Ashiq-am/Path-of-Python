# Python3 code to demonstrate
# segragation of keys and values
# using list comprehension + tuple()

# initializing list of dictionaries
test_list = [{'Nikhil' : 1, 'Akash' : 2},
			{'Nikhil' : 3, 'Akash' : 4}]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + tuple()
# to segregate keys and values
res = [tuple(i["Nikhil"] for i in test_list), tuple(i["Akash"]
										for i in test_list)]

# printing result
print("The segregated keys and values : " + str(res))

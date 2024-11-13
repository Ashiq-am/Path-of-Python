# Python3 code to demonstrate working of
# Test Record existance in Dictionary
# Using filter() + lambda

# initializing list
test_list = [{ 'name' : 'Nikhil', 'age' : 22},
			{ 'name' : 'Akshat', 'age' : 23},
			{ 'name' : 'Akash', 'age' : 23}]


# printing original list
print("The original list is : " + str(test_list))

# initializing key and value
test_key = 'name'
test_val = 'Nikhil'

# Test Record existance in Dictionary
# Using filter() + lambda
res = filter(lambda sub: test_val in sub.values(), test_list)
if len(list(res)):
	res = True
else :
	res = False

# printing result
print("Does key value contain in dictionary list : " + str(res))

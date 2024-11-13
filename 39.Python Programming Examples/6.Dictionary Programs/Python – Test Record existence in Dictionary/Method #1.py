# Python3 code to demonstrate working of
# Test Record existance in Dictionary
# Using any() + generator expression

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
# Using any() + generator expression
res = any(sub[test_key] == test_val for sub in test_list)

# printing result
print("Does key value contain in dictionary list : " + str(res))

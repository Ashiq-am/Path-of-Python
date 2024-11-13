# Python3 code to demonstrate working of
# Check List elements from Dictionary List
# Using loop

# helpr_func
def check_ele(ele, test_list):

	for sub in test_list:
		for item in sub.values():
			if ele == item:
				return True
	return False

# initializing list
test_list = [{'Name' : 'Apple', 'Price' : 18, 'Color' : 'Red'},
			{'Name' : 'Mango', 'Price' : 20, 'Color' : 'Yellow'},
			{'Name' : 'Orange', 'Price' : 24, 'Color' : 'Orange'},
			{'Name' : 'Plum', 'Price' : 28, 'Color' : 'Red'}]

# printing original list
print("The original list is : " + str(test_list))

# initializing Values list
val_list = ['Yellow', 'Red', 'Orange', 'Green']

# Check List elements from Dictionary List
# Using loop
res = []
for ele in val_list:
	res.append(check_ele(ele, test_list))

# printing result
print("The Association list in Order : " + str(res))

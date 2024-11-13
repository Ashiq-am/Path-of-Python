# Python3 code to demonstrate working of
# Extracting Priority Elements in Tuple List
# Using List comprehension + <code>index()

# initializing list
test_list = [(7, 1), (6, 4), (4, 7), (1, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Priority list
prior_list = [6, 4, 7, 1]

# Extracting Priority Elements in Tuple List
# Using List comprehension + <code>index()
res = [sub[0] if prior_list.index(sub[0]) < prior_list.index(sub[1])
			else sub[1] for sub in test_list]

# printing result
print("The extracted elements are : " + str(res))

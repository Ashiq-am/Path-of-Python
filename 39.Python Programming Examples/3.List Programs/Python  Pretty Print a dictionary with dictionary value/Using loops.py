# Python3 code to demonstrate working of
# Pretty Print a dictionary with dictionary value
# Using loops

# initializing dictionary
test_dict = {'gfg' : {'rate' : 5, 'remark' : 'good'}, 'cs' : {'rate' : 3}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using loops to Pretty Print
print("The Pretty Print dictionary is : ")
for sub in test_dict:
	print (sub)
	for sub_nest in test_dict[sub]:
		print (sub_nest, ':', test_dict[sub][sub_nest])

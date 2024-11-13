# Python program to remove space from keys

# creating a dictionary of type string

Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
				'P 0 3 ': 'Soft Computing'};

# removing spaces from keys
# storing them in sam dictionary
Product_list = {x.replace(' ', ''): v
	for x, v in Product_list.items()}

# printing new dictionary
print (" New dictionary : ", Product_list)

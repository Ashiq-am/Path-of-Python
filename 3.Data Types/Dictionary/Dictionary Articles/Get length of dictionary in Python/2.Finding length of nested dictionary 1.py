# Python program to find the
# length of the nested dictionary


# A nested dictionary

dict2 ={
	'Name':'Steve',
	'Age':30,
	'Designation':'Programmer',
	'address':
			{
		'Street':'Brigade Road',
		'City':'Bangalore',
		'Country':'India'
			}
	}

# total length = length of outer dict +
# length of inner dict
length = len(dict2)+len(dict2['address'])

print("The length of the nested dictionary is ", length)

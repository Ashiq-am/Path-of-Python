# use of dict.get() in multidimensional dictionary

dict = {'emp1': {'Name': {'First Name': 'Joe',
						'Last Name': 'tribiani'},
				'age': 32},
		'emp2': {'Name': {'First Name': 'Mark',
						'Last Name': 'Adam'},
				'age': 20},
		'emp3': {'Name': {'First Name': 'luci',
						'Last Name': 'truk'},
				'age': 47},
		}




# return Not Found if emp2 is not found
# or Name is not Found or Last name is not found
print(dict.get('emp2', {}).get('Name', {}).get('Last Name','Not Found'))

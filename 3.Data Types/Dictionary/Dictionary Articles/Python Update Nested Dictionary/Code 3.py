# an employee record
Employee = {
	'emp1': {
		'name': 'Lisa',
		'age': '29',
		'Designation':'Programmer'
			},
		'emp2': {
			'name': 'Steve',
			'age': '25',
			'Designation':'HR'
				}
			}

# updating in the way similar to
# simple dictionary
Employee['emp1']['name']='Kate'

# adding new key-value pair to first
# employee record
Employee['emp1']['salary']= 56000

print(Employee)

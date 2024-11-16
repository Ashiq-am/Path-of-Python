# initialising the data
data = {
	'company': 'XYZ pvt ltd',
	'location': 'London',
	'info': {
		'president': 'Rakesh Kapoor',
		'contacts': {
			'email': 'contact@xyz.com',
			'tel': '9876543210'
		}
	},
	'employees': [
		{'name': 'A'},
		{'name': 'B'},
		{'name': 'C'}
	]
}

# converting the data to dataframe
df = pd.json_normalize(data)

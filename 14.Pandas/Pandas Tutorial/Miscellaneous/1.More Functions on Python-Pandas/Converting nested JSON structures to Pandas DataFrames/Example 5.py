data = [
	{
		'id': '001',
		'company': 'XYZ pvt ltd',
		'location': 'London',
		'info': {
			'president': 'Rakesh Kapoor',
			'contacts': {
					'email': 'contact@xyz.com',
					'tel': '9876543210'
			}
		}
	},
	{
		'id': '002',
		'company': 'PQR Associates',
		'location': 'Abu Dhabi',
		'info': {
			'president': 'Neelam Subramaniyam',
			'contacts': {
					'email': 'contact@pqr.com',
					'tel': '8876443210'
			}
		}
	}
]

pd.json_normalize(data)

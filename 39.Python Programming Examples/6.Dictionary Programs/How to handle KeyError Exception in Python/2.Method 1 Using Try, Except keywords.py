# Creating a Dictionary
subjects = {'Sree': 'Maths',
			'Ram': 'Biology',
			'Shyam': 'Science',
			'Abdul': 'Hindi'}
# try block
try:
	print('subject of Fharan is:',
		subjects['Fharan'])
# except Block
except KeyError:
	print("Fharan's records doesn't exist")

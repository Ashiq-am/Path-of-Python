# Example of dict.get() with multidimensional dict
dict = {'India': {'captain': 'Virat', 'Batsman': 'Rohit',
				'Bolwer': 'Bumrah'},
		'England': {'captain': 'Root', 'Batsman': 'Buttler',
					'Bolwer': 'anderson'},
		'Australia': {'captain': 'Paine', 'Batsman': 'Warner',
					'Bolwer': 'Starck'},
		'Pakistan': {'captain': 'Babar', 'Batsman': 'Hafiz',
					'Bolwer': 'Aamir'},
		'West Indies': {'captain': 'Pollard', 'Batsman': 'Gayle',
						'Bolwer': 'Narayan'}
		}

# find batsman for new zealand
# return Not Found if not exists in dict
# if new zealand not found in dict will result in error
print(dict.get('new zealand').get('Batsman', 'Not Found'))

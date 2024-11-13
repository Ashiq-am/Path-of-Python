dict = {
	'Geeks': {
		'for': {
			'Geeks': 1,
			'CS': 2,
			'IT': 3
		},
		'GFG': {
			'Courses': {
				'DSA': 4,
				'Algorithms': 5
			},
			'Quiz': 6
		}
	}
}
for key1, value1 in dict.items():
	print(f"Level 1: {key1}")
	for key2, value2 in value1.items():
		print(f"\tLevel 2: {key2}")
		for key3, value3 in value2.items():
			print(f"\t\tLevel 3: {key3} - {value3}")

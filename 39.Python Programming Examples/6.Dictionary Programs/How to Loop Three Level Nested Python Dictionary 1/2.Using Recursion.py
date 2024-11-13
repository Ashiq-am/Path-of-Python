def recursiveFn(d, level=1):
	for key, value in d.items():
		print('\t' * (level - 1) + f'Level {level}: {key}', end=' ')
		if isinstance(value, dict):
			print()
			if level == 3:
				print('\t' * level + f'- {value}')
			else:
				recursiveFn(value, level + 1)
		else:
			print(f'- {value}')
dict_data = {
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
recursiveFn(dict_data)

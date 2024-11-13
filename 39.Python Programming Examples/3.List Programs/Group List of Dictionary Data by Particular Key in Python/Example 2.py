# import required methods
from itertools import groupby
from operator import itemgetter

# dictionary
students = [
	{'mark': '65', 'grade': 'C'},
	{'mark': '86', 'grade': 'A'},
	{'mark': '73', 'grade': 'B'},
	{'mark': '49', 'grade': 'D'},
	{'mark': '91', 'grade': 'A'},
	{'mark': '79', 'grade': 'B'}
]

# Sort students data by grade key.
students = sorted(students,
				key = itemgetter('grade'))

# Display data grouped by grade
for key, value in groupby(students,
						key = itemgetter('grade')):
	print(key)
	for k in value:
		print(k)

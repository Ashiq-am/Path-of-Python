# import defaultdict module
from collections import defaultdict

# declare a list with student data
input = [('bhanu', 'html'),
		('bhanu', 'php'),
		('suma', 'python'),
		('rasmi', 'java'),
		('suma', 'html/csscss')]

# declare a default dict
data = defaultdict(list)

# append to the dictinary
for key, value in input:
	data[key].append(value)

# display
print(data.items())

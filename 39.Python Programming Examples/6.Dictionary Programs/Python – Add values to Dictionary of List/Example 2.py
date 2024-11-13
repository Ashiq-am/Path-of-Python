# import defaultdict module
from collections import defaultdict

# declare a list with student data with age
input = [('bhanu', 10), ('uma', 12), ('suma', 11)]

# declare a default dict
data = defaultdict(list)

# append to the dictinary
for key, value in input:
	data[key].append(value)

# display
print(data.items())

# import orderedDict module
from collections import OrderedDict

# declare a dictionary of tuple with student data
data = {('bhanu', 10): 'student1',
		('uma', 12): 'student4',
		('suma', 11): 'student3',
		('ravi', 11): 'student2',
		('gayatri', 9): 'student5'}

# sort student dictionary of tuple based
# on items using OrderedDict
print(OrderedDict(sorted(data.items())))
